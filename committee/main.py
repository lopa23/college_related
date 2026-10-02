"""
The Committee — a multi-persona critique engine for admissions application
materials, modeled on VerticalResearchGroup/Gauntlet's divergence/convergence
design (https://github.com/VerticalResearchGroup/Gauntlet).

Divergence: each persona (admissions officer, financial aid officer, etc.)
critiques the draft independently, once per configured temperature.
Convergence: the Synthesizer takes every combination of one critique per
persona and produces a prioritized Admissions Strategy Memo for each combo.

Usage:
    python main.py [-c config_base.toml] [-o outputs] context.md draft.md

See README.md in this folder for the full concept and setup instructions.
"""
import argparse
import itertools
import os
import sys
from pathlib import Path

# On some Windows setups, httpx's default TLS verification via `truststore`
# hits a self-recursion bug (ssl.SSLContext.verify_mode). Pointing it at
# certifi's cert bundle instead avoids that code path. Must happen before
# anthropic/httpx are imported.
if "SSL_CERT_FILE" not in os.environ:
    try:
        import certifi
        os.environ["SSL_CERT_FILE"] = certifi.where()
    except ImportError:
        pass

try:
    import tomllib
except ModuleNotFoundError:
    import tomli as tomllib  # Python < 3.11

from dotenv import load_dotenv
import anthropic


def read_text(path: Path) -> str:
    if path.suffix.lower() == ".pdf":
        try:
            from pypdf import PdfReader
        except ImportError:
            sys.exit(
                f"{path} is a PDF but pypdf isn't installed. "
                "Run: pip install pypdf"
            )
        reader = PdfReader(str(path))
        return "\n".join(page.extract_text() or "" for page in reader.pages)
    return path.read_text(encoding="utf-8")


def load_config(config_path: Path) -> dict:
    with open(config_path, "rb") as f:
        return tomllib.load(f)


def persona_prompt(personas_dir: Path, name: str) -> str:
    p = personas_dir / f"{name}.md"
    if not p.exists():
        sys.exit(f"Persona file not found: {p}")
    return p.read_text(encoding="utf-8")


def run_critique(client, model: str, system_prompt: str, context: str, draft: str,
                  temperature: float) -> str:
    message = client.messages.create(
        model=model,
        max_tokens=4096,
        temperature=temperature,
        system=system_prompt,
        messages=[{
            "role": "user",
            "content": (
                "## Context (target school / what to evaluate)\n\n"
                f"{context}\n\n"
                "## Document to critique\n\n"
                f"{draft}"
            ),
        }],
    )
    return "".join(block.text for block in message.content if block.type == "text")


def run_synthesis(client, model: str, synth_prompt: str, reviews: dict[str, str]) -> str:
    body = "\n\n---\n\n".join(
        f"### Review from: {persona}\n\n{text}" for persona, text in reviews.items()
    )
    message = client.messages.create(
        model=model,
        max_tokens=4096,
        temperature=0.5,
        system=synth_prompt,
        messages=[{"role": "user", "content": body}],
    )
    return "".join(block.text for block in message.content if block.type == "text")


def main():
    parser = argparse.ArgumentParser(description="Run The Committee on a draft.")
    parser.add_argument("context", type=Path, help="Target school / evaluation context (.md, .txt, or .pdf)")
    parser.add_argument("draft", type=Path, help="The application material to critique (.md, .txt, or .pdf)")
    parser.add_argument("-c", "--config", type=Path, default=Path(__file__).parent / "config_base.toml")
    parser.add_argument("-o", "--output", type=Path, default=Path(__file__).parent / "outputs")
    args = parser.parse_args()

    load_dotenv()
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        sys.exit(
            "ANTHROPIC_API_KEY not set. Put it in a .env file in this folder "
            "(committee/.env) or export it in your shell."
        )
    client = anthropic.Anthropic(api_key=api_key)

    cfg = load_config(args.config)
    model = cfg.get("model", "claude-sonnet-5")
    temperatures = cfg.get("temperatures", [0.3])
    personas_dir = Path(__file__).parent / "personas"

    persona_entries = cfg["personas"]
    if len(temperatures) ** len(persona_entries) > 81:
        print(
            f"Warning: {len(temperatures)} temperatures x {len(persona_entries)} "
            f"personas = {len(temperatures) ** len(persona_entries)} synthesis combos. "
            "Consider fewer personas or a single temperature (see README's note on this)."
        )

    context_text = read_text(args.context)
    draft_text = read_text(args.draft)

    reviews_dir = args.output / "expert_reviews"
    synth_dir = args.output / "syntheses"
    reviews_dir.mkdir(parents=True, exist_ok=True)
    synth_dir.mkdir(parents=True, exist_ok=True)

    # --- Divergence: each persona critiques at each configured temperature ---
    run_paths: dict[str, list[Path]] = {}
    for entry in persona_entries:
        name, short = entry["name"], entry["short"]
        system_prompt = persona_prompt(personas_dir, name)
        persona_out = reviews_dir / short
        persona_out.mkdir(parents=True, exist_ok=True)
        run_paths[short] = []
        for i, temp in enumerate(temperatures, start=1):
            out_path = persona_out / f"run_{i}.md"
            run_paths[short].append(out_path)
            if out_path.exists():
                print(f"[skip] {out_path} already exists")
                continue
            print(f"[critique] {short} (temp={temp}) -> {out_path}")
            review = run_critique(client, model, system_prompt, context_text, draft_text, temp)
            out_path.write_text(review, encoding="utf-8")

    # --- Convergence: synthesize every combination of one run per persona ---
    shorts = list(run_paths.keys())
    for combo in itertools.product(*[range(len(temperatures)) for _ in shorts]):
        combo_name = "__".join(f"{shorts[i]}_{combo[i] + 1}" for i in range(len(shorts)))
        combo_dir = synth_dir / combo_name
        synthesis_path = combo_dir / "SYNTHESIS.md"
        if synthesis_path.exists():
            print(f"[skip] {synthesis_path} already exists")
            continue
        combo_dir.mkdir(parents=True, exist_ok=True)
        reviews = {}
        for i, short in enumerate(shorts):
            review_text = run_paths[short][combo[i]].read_text(encoding="utf-8")
            reviews[short] = review_text
            (combo_dir / f"{short}.md").write_text(review_text, encoding="utf-8")
        print(f"[synthesize] {combo_name}")
        synth_prompt = persona_prompt(personas_dir, cfg.get("synthesizer", "synthesizer"))
        synthesis = run_synthesis(client, model, synth_prompt, reviews)
        synthesis_path.write_text(synthesis, encoding="utf-8")

    print(f"\nDone. Reviews in {reviews_dir}, syntheses in {synth_dir}.")


if __name__ == "__main__":
    main()
