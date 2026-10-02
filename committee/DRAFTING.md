# Drafting Against the Committee — The Concept

## The problem it solves

The Committee (`main.py`) is a critique engine. It takes an application document and stress-tests it from several reviewer perspectives, then a Synthesizer merges the surviving concerns into an action plan. But a critique engine is only as useful as what it's given to critique. If a first draft has a structural flaw — a generic "why us" paragraph, a financial-aid blind spot, an unverified claim — the Committee will catch it, but only *after* you've spent the time (and API calls) running the full review.

`draft_generator.py` ("The Strategist") exists to make the first draft defensible before it reaches the Committee.

## The core move: writing against known reviewers

A naive draft generator takes a rough idea and expands it into prose. The Strategist does something different: it is given the full persona collection — the same reviewers who will later critique the output — and asked to *write against them*.

This is not generic essay-writing advice. It is adversarial drafting. The Strategist reads each reviewer's stated evaluation criteria (all grounded in this project's own admissions research — see each file in `personas/`) and makes deliberate choices to pre-empt the objections each one would raise.

Compare:

> *Vague:* "I want to attend State University because of its strong computer science program."
>
> *Adversarially grounded:* "I want to work in Professor [X]'s robotics lab, which runs the specific research track I've already started independently with [concrete prior work] — this is the kind of specific proper-noun detail the admissions-officer persona flags as the difference between a real 'why us' and a template with the school name swapped in."

The second version exists because the Strategist knew the admissions-officer persona was coming, and knew exactly what it checks for.

## What the seed is (and isn't)

The seed (set in `config_base.toml`) is the rough idea — which school, what the student actually wants to say, what financial/ED constraints apply — not a polished argument. Over-specifying it limits the Strategist's ability to find the strongest framing for that idea against the reviewers it knows are coming.

## The human step is load-bearing

The output is a markdown kernel (`draft_kernel.md`), not a submission. The Strategist is instructed to mark anything it can't verify as `[VERIFY: ...]` rather than inventing a plausible-sounding fact, a real program name, or a test-score policy — but it is still a language model, and a human must read the draft critically, check every verify-marker, and ground anything the Strategist got wrong or invented before this goes anywhere near a real application or the Committee.

## Where it sits

```
Seed (config) + optional baseline draft/context
            │
            ▼
     The Strategist          ← produces a defensively-drafted kernel
            │
            ▼
     Human edits             ← grounds every [VERIFY: ...] marker, fixes facts
            │
            ▼
     The Committee (main.py) ← the real multi-persona critique + synthesis
            │
            ▼
     Strategy memos
```

The Strategist and the Committee share the same `personas/` collection via the same config file. That shared reviewer set is what makes this a coherent two-stage pipeline rather than two unrelated scripts.

---

# How to Run It

## Prerequisites

* `ANTHROPIC_API_KEY` in a `.env` file inside `committee/` (or your shell environment).
* `pip install -r requirements.txt` (see root `README.md` of this folder for the full install note — do not run installs yourself if you've had install issues before; ask for the manual command instead).
* A config file (e.g. `config_base.toml`) with a `seed` key in addition to the usual `[[personas]]` and `synthesizer` keys.

## The command

```bash
python draft_generator.py [options] [baseline]
```

| Argument | What it is | Default |
|---|---|---|
| `baseline` | Optional existing draft or context file (`.md`, `.txt`, or `.pdf`) — positional | none |
| `-c` / `--config` | Config file | `config_base.toml` in this folder |
| `-o` / `--output` | Output directory — `draft_kernel.md` is written here | `outputs/` in this folder |

### Examples

```bash
# Simplest — uses config_base.toml's seed, no baseline, writes to outputs/
python draft_generator.py

# Revise an existing rough draft against the same seed
python draft_generator.py -o outputs/yale_why_essay drafts/yale_rough_v1.md
```

## After you have the kernel

1. Open `outputs/draft_kernel.md`. Read it critically.
2. Resolve every `[VERIFY: ...]` marker against real facts — don't skip this.
3. Feed the grounded result into the Committee:

```bash
python main.py -o outputs/yale_why_essay context.md outputs/yale_why_essay/draft_kernel.md
```

Using the same `-c` config file keeps the Strategist and the Committee working from the same reviewer set.
