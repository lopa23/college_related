# Index — what's in each file

For folder layout, see `README.md`/`CLAUDE.md`. This file is a per-document index: what each file actually contains, one line each, so you can find the right source without opening everything. Grouped by folder, in the same order as the structure doc.

## Root

- **`College Advising Knowledge Base & Triage Engine.md`** — the core task/archetype-organized triage framework for advising a given applicant profile; the entry point for "what do I do with this student's situation."

## qualitative_insights/ — practitioner-voice content

- **`Admissions Book Reference & Profile Query Guide.md`** — synthesis of admissions-strategy books (Selingo, Tough, Harberson, Sabky, etc.), organized by theme for profile-querying.
- **`Admissions Officer AMA Insights & Profile Query Guide.md`** — six Reddit/IAmA AMA threads from self-identified current/former admissions officers (Penn's official team, Cornell, an anonymous Ivy, a ~50%-admit LAC, Vanderbilt), with a source-credibility ledger and cross-corroboration flags.
- **`MIT Admissions Blog Insights & Process Guide.md`** — ~15 posts from MIT's official admissions blog (2007–2024), including Dean Schmill's own rationale for reinstating testing and the disclosed post-SFFA enrollment shift.
- **`Admissions Office Blogs & Podcasts Insights.md`** — Georgia Tech's and Tulane's official blogs, plus full-transcript material from Yale's and Dartmouth's official admissions podcasts; includes the cross-school "who tracks demonstrated interest" split.
- **`More University Admissions Blogs (UChicago, Vanderbilt, Case Western, Rochester).md`** — extends the blog coverage to four more schools; flags that UChicago's blog is currently offline and Case Western's was shut down in 2019, reconstructed via Wayback Machine.
- **`Admissions Office Webinars & Virtual Info Session Insights.md`** — 13 universities' own webinar/YouTube presence; Yale's is the strongest, MIT's/Stanford's are surprisingly thin.
- **`Independent Admissions Consultancy Webinars.md`** — 11 commercial counseling firms (IvyWise, Crimson, Top Tier, etc.); finds credential-verification and content-verification are separate bars most firms only clear the first of.
- **`books/`** — source material backing the book-reference file above.

## institutional_data/ — hard numbers

- **`School Admissions Data Reference (CDS + IPEDS).md`** — the core numeric reference: selectivity/test ranges, CDS factor weightings, cost/outcomes, UC by-discipline data, non-UC CS-program admit rates, direct-admit-vs-unified structure (§4c), and a 2014–2024 admit-rate trend for 60 schools.
- **`SFFA Lawsuit Data (Harvard & UNC).md`** — disclosed Harvard/UNC admissions data from the SFFA litigation (raw admit rates by race, ALDC preference rates, personal-rating disparities), with established-vs-contested labeling.
- **`NACAC State of College Admission Data.md`** — industry-wide survey data on what factors colleges say they weight; documents the test-score-importance collapse (56%→5% "considerable importance," 2012–2023).
- **`Common App Aggregate Data Trends.md`** — platform-wide application-volume trends through the 2025–26 cycle (first-gen/fee-waiver growth, international decline, geographic shifts).
- **`Parchment Cross-Admit Yield Data.md`** — head-to-head "which school wins" revealed-preference data (e.g. MIT beats Harvard 63–37); flags that Parchment's aggregate rankings are stuck on stale 2021-cycle data.
- **`College Scorecard Field-of-Study Earnings (CS & Engineering).md`** — federal major-level (not whole-institution) earnings data; CMU's CS program tops the national list at $161,723 median 1-year earnings.
- **`State Percent Plans & Guaranteed Admission Policies.md`** — Texas Top 10% Rule, California's ELC, Florida's Talented Twenty, traced to their origin as race-neutral responses to affirmative-action bans.
- **`school_data/`** — raw pulls and build scripts backing the files above (CDS/IPEDS JSON for 60 schools, the full national IPEDS record for ~2,000 institutions, UC Tableau data, Scorecard field-of-study CSVs).

## applicant_profiles/ — the archive itself

- **`combined_profiles.json`** — ~2,402 real applicant profiles from r/collegeresults, r/chanceme, and College Confidential; ~1,215 joined against school-level admissions data.
- **`processeddata.csv`**, **`reditt_results.md`** — intermediate/raw scrape outputs feeding the combined archive.
- **`applicant_profile_to_query/`** — tooling for querying the archive by profile characteristics.

## pipeline/ — scraper code and state

- **`redditt_scrapper.py`** — the scraper itself.
- **`enrichment_progress.json`**, **`cc_enrichment_progress.json`**, **`chanceme_enrichment_progress.json`**, **`rows_index.json`** — checkpoint/progress state for resumable scraping and enrichment runs.

---

*Keep this in sync with `README.md`/`CLAUDE.md` when files are added, removed, or renamed — those two cover the folder tree, this one covers what's actually inside each file.*
