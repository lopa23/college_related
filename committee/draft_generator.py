"""
The Strategist — drafts an application element (essay, activities list entry,
college-list rationale, financial-aid narrative) written *against* the same
committee personas that will later critique it in main.py.

This is the adversarial-drafting front-end described in DRAFTING.md, modeled
on Gauntlet's idea_generator.py: instead of a blank-page draft, the seed idea
is expanded into something that has already anticipated each reviewer's
objections.

Usage:
    python draft_generator.py [-c config_base.toml] [-o outputs] [baseline.md]

The config file must have a `seed` key (see config_base.toml for the format).
`baseline` is optional: an existing rough draft, a prior essay, or relevant
context (e.g. the student's own triage-engine notes) to revise against.
"""
import argparse
import os
import sys
from pathlib import Path

try:
    import tomllib
except ModuleNotFoundError:
    import tomli as tomllib

from dotenv import load_dotenv
import anthropic


def read_text(path: Path) -> str:
    if path.suffix.lower() == ".pdf":
        try:
            from pypdf import PdfReader
        except ImportError:
            sys.exit(f"{path} is a PDF but pypdf isn't installed. Run: pip install pypdf")
        reader = PdfReader(str(path))
        return "\n".join(page.extract_text() or "" for page in reader.pages)
    return path.read_text(encoding="utf-8")


def main():
    parser = argparse.ArgumentParser(description="Draft an application element against the committee's known criteria.")
    parser.add_argument("baseline", type=Path, nargs="?", default=None,
                         help="Optional existing draft or context file (.md, .txt, or .pdf)")
    parser.add_argument("-c", "--config", type=Path, default=Path(__file__).parent / "config_base.toml")
    parser.add_argument("-o", "--output", type=Path, default=Path(__file__).parent / "outputs")
    args = parser.parse_args()

    load_dotenv()
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        sys.exit("ANTHROPIC_API_KEY not set. Put it in committee/.env or export it in your shell.")
    client = anthropic.Anthropic(api_key=api_key)

    with open(args.config, "rb") as f:
        cfg = tomllib.load(f)

    seed = cfg.get("seed")
    if not seed:
        sys.exit(
            f"No `seed` key found in {args.config}. Add one — see the `seed` "
            "example in config_base.toml. The seed is the rough direction "
            "(what you want to argue, which school, what's at stake), not a "
            "polished draft."
        )

    model = cfg.get("model", "claude-sonnet-5")
    personas_dir = Path(__file__).parent / "personas"

    persona_blocks = []
    for entry in cfg["personas"]:
        p = personas_dir / f"{entry['name']}.md"
        persona_blocks.append(f"## Reviewer: {entry['name']}\n\n{p.read_text(encoding='utf-8')}")
    synth_path = personas_dir / f"{cfg.get('synthesizer', 'synthesizer')}.md"
    persona_blocks.append(f"## Synthesizer\n\n{synth_path.read_text(encoding='utf-8')}")
    know_your_reviewers = "\n\n---\n\n".join(persona_blocks)

    system_prompt = f"""You are The Strategist. Your job is to draft an application \
element (an essay, an activities-list entry, a college-list rationale, or a \
financial-aid narrative — whatever the seed below asks for) that has already \
been written to hold up against a specific panel of reviewers who will \
critique it after you're done.

This is adversarial drafting, not generic advice. Read each reviewer's stated \
evaluation criteria below and make deliberate choices that pre-empt the \
objections each one will raise — specific proper nouns instead of vague \
praise, rigor read in context instead of raw numbers, a real financial-aid \
posture instead of an assumption, international context handled explicitly \
if relevant.

Do not invent specific facts about real schools, named programs, or test \
score policies that you are not given — if something needs a real number \
or citation, mark it clearly as [VERIFY: ...] rather than inventing a \
plausible-sounding one. The human reviewing your draft will ground these \
markers before this goes anywhere near the actual committee critique.

# Know Your Reviewers

{know_your_reviewers}
"""

    user_content = f"## Seed (rough direction, not a polished argument)\n\n{seed}"
    if args.baseline:
        user_content += f"\n\n## Baseline / existing material to revise against\n\n{read_text(args.baseline)}"

    print("Drafting...")
    message = client.messages.create(
        model=model,
        max_tokens=4096,
        temperature=0.7,
        system=system_prompt,
        messages=[{"role": "user", "content": user_content}],
    )
    draft = "".join(block.text for block in message.content if block.type == "text")

    args.output.mkdir(parents=True, exist_ok=True)
    out_path = args.output / "draft_kernel.md"
    out_path.write_text(draft, encoding="utf-8")
    print(f"Wrote {out_path}")
    print(
        "\nNext: open it, check every [VERIFY: ...] marker against real facts, "
        "edit as needed, then feed it into main.py as the draft to critique."
    )


if __name__ == "__main__":
    main()
