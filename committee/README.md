# The Committee 🎓

A multi-persona critique engine for stress-testing a specific application document — an essay, an activities-list entry, a college list, a financial-aid strategy — against reviewer personas grounded in this project's own admissions research.

Modeled on [VerticalResearchGroup/Gauntlet](https://github.com/VerticalResearchGroup/Gauntlet), a research-proposal critique engine. The Gauntlet subjects a research proposal to simulated expert reviewers; the Committee does the same thing to an application document, using reviewers built from the real admissions-officer testimony, FERPA file reviews, and institutional data already gathered in `qualitative_insights/` and `institutional_data/` elsewhere in this repo — not generic personas invented for this folder.

Instead of a single generic "review my essay" pass, the Committee explodes the critique the way a real file actually gets read by multiple, differently-motivated people:

- **Divergence:** each persona critiques the document independently (optionally multiple times at different temperatures — conservative, balanced, divergent takes).
- **Convergence (The Flywheel):** a Synthesizer takes every combination of one critique per persona and produces a prioritized **Admissions Strategy Memo** for each combination, naming the highest-leverage fix and any real tradeoffs the reviewers disagree on.

## 🗂 Project Structure

```
committee/
├── inputs/                              # put the document(s) you want reviewed here (gitignored)
│   ├── context.md                       # the target school / what's being evaluated
│   └── draft.md                         # the actual essay / activities list / college list / profile
├── personas/
│   ├── admissions_officer_elite_private.md     # holistic, sub-10%-admit private school
│   ├── admissions_officer_public_flagship.md   # UC-style large public, formula + context
│   ├── financial_aid_officer.md                # FAFSA/CSS, ED risk, need-blind/need-aware
│   ├── independent_counselor_skeptic.md        # myth-busting, yield management, proportionality
│   ├── international_admissions_specialist.md  # curriculum context, need-blind gap, right denominator
│   └── synthesizer.md                          # the Strategy Lead system prompt
├── outputs/                             # generated reviews + syntheses (gitignored — real application
│   ├── expert_reviews/                  #   material is personal; keep it local)
│   │   ├── ao_private/                  #   run_1.md, run_2.md, ... (one per configured temperature)
│   │   ├── ao_public/
│   │   ├── aid/
│   │   ├── skeptic/
│   │   └── intl/
│   └── syntheses/                       # one self-contained folder per combination
│       └── ao_private_1__ao_public_1__.../
│           ├── SYNTHESIS.md
│           └── (copies of the source reviews that fed it)
├── draft_generator.py                   # optional front-end: drafts a kernel written against these same personas
├── DRAFTING.md                          # the adversarial-drafting concept + how to run draft_generator.py
├── config_base.toml                     # persona & synthesizer selection, model, temperatures, seed
├── requirements.txt
├── .env                                 # ANTHROPIC_API_KEY (gitignored, you create this)
└── main.py                              # orchestration & combination logic
```

## 🧠 The Committee (grounded in this project's own research)

- **Admissions Officer — Elite Private University:** reads rigor only in the context of the applicant's own school, weighs roughly 40% academic / 30% activities / 30% "texture," and critiques the way real FERPA file reviews in `qualitative_insights/YouTube College Counseling Video Insights.md` show readers actually diverge on the same file.
- **Admissions Officer — Large Public Flagship:** recalculates GPA from a narrower set of terms the way the UC system actually does, doesn't use testing or recommendation letters at all, and corrects viral myths a current UC officer has already had to publicly debunk.
- **Financial Aid Officer:** evaluates purely on cost exposure — FAFSA vs. CSS Profile, the real risk of a binding Early Decision commitment, need-blind vs. need-aware status for international applicants.
- **Independent Counselor (Skeptic):** corrects yield-management confusion, prestige-anxiety, and AI-in-admissions myths this project's own research has already found to be overstated or false.
- **International Admissions Specialist:** catches every place a draft silently assumes a domestic applicant — curriculum-context, the need-blind gap, the right admit-rate denominator.

Every persona file names the specific project file and section its criteria come from. If this project's research changes or grows, update the persona, not just this README.

## 🚀 The Logic Flow

1. **Ingestion:** `main.py` reads `context.md` (what's being evaluated, and for which school) and `draft.md` (the actual document).
2. **The Committee (Phase 1 — Divergence):** each configured persona critiques the document once per configured temperature.
3. **The Flywheel (Phase 2 — Convergence):** the Synthesizer produces one Admissions Strategy Memo per combination of critiques, each a self-contained folder with its sources.
4. **Idempotent resume:** re-running `main.py` skips any review or synthesis that already exists on disk — safe to re-run after a rate limit or interruption.

## 💡 The Strategist (Optional Front-End)

Before running the Committee, `draft_generator.py` can produce the draft itself — given a rough seed (which school, what you want to argue, ED/aid constraints) it drafts something already written *against* the same personas, anticipating their critiques before they happen. See [DRAFTING.md](DRAFTING.md).

## 🛠 Usage

1. **Install dependencies** (if you've had pip-install issues crash your machine before, run this yourself from a terminal rather than asking an agent to run it for you):
   ```bash
   pip install -r requirements.txt
   ```
2. **Add your API key** to `committee/.env`:
   ```
   ANTHROPIC_API_KEY=sk-ant-...
   ```
3. **Put your material in `inputs/`** — a `context.md` describing the target school and what's being evaluated, and a `draft.md` with the actual document.
4. **Edit `config_base.toml`** to select which personas to run.
5. **Run it:**
   ```bash
   python main.py inputs/context.md inputs/draft.md
   ```
   Use `-o` for a custom output folder, e.g. `-o outputs/yale_why_essay`.
6. The default `temperatures = [0.3]` gives one critique per persona and one synthesis. Raise it to `[0.3, 0.7, 1.0]` for conservative/balanced/divergent takes per persona — but with 5 personas that's 3⁵ = 243 synthesis combinations; trim personas in the config first if you do this.

## 🎛️ Tuning the Synthesizer

`personas/synthesizer.md` is the one file you should edit per use case. Tell it what you actually want out of a synthesis: a prioritized fix list for an essay close to a deadline, a brutal tradeoff analysis for an ED decision, or a cost-first read for a financial-aid-sensitive family. The default prompt asks for a "golden thread" plus explicit tradeoffs — adjust it if your priority is different.

## ⚠️ Privacy note

`inputs/` and `outputs/` are gitignored by default. This folder is designed to run on a real student's real essays, activities list, and financial situation — that material (and the AI's critique of it) should stay local, the same way `applicant_profile_to_query/` elsewhere in this repo is gitignored for the same reason. Don't remove those `.gitignore` entries without thinking about why they're there.

## 📄 Relationship to the rest of this repo

The Committee is a *consumer* of this project's research, not a new research pipeline. If a persona's claim turns out to be wrong, dated, or newly contradicted by something in `qualitative_insights/` or `institutional_data/`, fix the persona file — that keeps this folder's critiques as accurate as the knowledge base it's built on.
