# Parchment Cross-Admit Yield Data

> **What this is:** Revealed-preference data from Parchment (a company that processes transcript requests for millions of college applicants) on where students actually choose to enroll when they're admitted to **multiple** schools simultaneously — head-to-head "who wins" data between specific school pairs, plus an aggregate Elo-style ranking built from those matchups. The official product name is the **Parchment Student Choice College Rankings**; "Ultimate College Rankings" and "yield battle" are informal shorthand used by forums, not Parchment's own branding, and no Forbes/WSJ co-publishing partnership was found — this is Parchment's own product, not a syndicated media ranking.
>
> **Why this belongs in this project:** every admit-rate number elsewhere in this archive answers "how hard is it to get in." Nothing else answers **"when a student actually has a real choice between two specific schools, which one do they pick"** — a completely different, and arguably more decision-relevant, question for a student choosing between offers. Cross-reference the aggregate ranking against `Admissions Office Blogs & Podcasts Insights.md` §6 and the "match, not prestige" framing throughout the practitioner files — this data is a market-level counterpoint to that advice, showing what students actually do, not what they're advised to value.
>
> **Read the freshness caveat below before citing anything here as current.**

---

## 1. Data freshness — a real limitation, stated honestly

Parchment's **aggregate ranking table is currently stalled at the 2022 edition, built from the Fall 2021 admissions cycle** — roughly five years old as of this writing. Direct navigation of the live site across every recent year parameter (2023, 2024, 2025, 2026 editions) returned no data ("Sorry, we don't have any results for your query") — a site malfunction on Parchment's end, not a paywall. The **pairwise head-to-head comparison tool**, by contrast, is live and returns real percentages on demand today — but it carries no date stamp and no disclosed sample size, only a confidence interval, so its recency relative to the stalled aggregate table is unknown. Treat any secondary source citing a "2023/2024/2025 Parchment ranking" with real suspicion — the primary site currently serves no data for those years.

## 2. Most recent working aggregate ranking (2022 edition, Fall 2021 cycle, National Universities)

Elo-style score (1500 starting point, Monte Carlo path-randomization across 10,000 iterations — methodology unchanged since at least 2014), with matchup count (total student decisions observed) in parentheses:

| Rank | School | Elo score | Matchups |
|--:|:--|--:|--:|
| 1 | MIT | 2156 | 1,567 |
| 2 | Caltech | 2073 | 435 |
| 3 | Stanford | 2026 | 2,606 |
| 4 | Johns Hopkins | 1996 | 1,380 |
| 5 | Michigan (Ann Arbor) | 1960 | 28,304 |
| 6 | USC | 1956 | 6,358 |
| 7 | UCLA | 1953 | 10,749 |
| 8 | UC Berkeley | 1947 | 9,522 |
| 9 | University of Chicago | 1915 | 2,252 |
| 10 | Notre Dame | 1909 | 2,787 |
| 11 | Princeton | 1900 | 1,494 |
| 12 | UPenn | 1899 | 1,897 |
| 13 | Brown | 1895 | 1,661 |
| 14 | Columbia | 1874 | 1,387 |
| 15 | Rice | 1871 | 1,259 |
| 17 | Yale | 1856 | 1,836 |
| 19 | Northwestern | 1851 | 2,935 |

**Harvard does not appear in the top 20 of this edition** — a striking absence for a school normally treated as the top "prestige" brand, and not something the archive's admit-rate data alone would predict.

## 3. The Harvard/Princeton-vs-MIT/Stanford trend across editions

| Edition (admissions cycle) | #1 | #2 | #3 | Harvard's rank |
|:--|:--|:--|:--|:--|
| 2014 (2013 cycle) | Stanford (2493) | MIT (2457) | Harvard (2408) | 3rd |
| 2020 (2019 cycle) | MIT (2222) | Stanford (2047) | Michigan | not in top 5 shown |
| 2021 (2020 cycle) | MIT (2168) | Stanford (2134) | Northwestern | not in top 5 shown |
| 2022 (2021 cycle) | MIT (2156) | Caltech (2073) | Stanford (2026) | outside top 20 |

**MIT has held or gained the #1 spot in every recent working edition, while Harvard has fallen from #3 (2014) to outside the top 20 (2022 edition).** This is corroborated, directionally, by an independent (non-Parchment) commentary site, College Monte Carlo, which reaches the same conclusion synthesizing Parchment data alongside other sources — though that site itself flags the analysis as not rigorously longitudinal, and notes Parchment's user base (whoever uses its transcript-sending service) isn't necessarily a representative sample of all admitted students everywhere.

## 4. Specific head-to-head win rates (live comparison tool, pulled directly)

| Matchup | Result | 95% confidence interval |
|:--|:--|:--|
| Harvard vs. MIT | **MIT wins, 63%–37%** | MIT: 54.8–71.1%; Harvard: 28.9–45.2% |
| Harvard vs. Stanford | **Harvard wins, 65%–35%** | Harvard: 59.0–70.0%; Stanford: 30.0–41.0% |
| UCLA vs. UC Berkeley | **UCLA wins, 61%–39%** | UCLA: 59.5–62.9%; Berkeley: 37.1–40.5% |

**A discrepancy worth flagging:** one secondary web source claimed "MIT wins 3 of 4 HYPSM matchups, losing only to Harvard" — the opposite of what the live tool actually shows (MIT beats Harvard 63–37 head-to-head). That secondary claim should be treated as unverified or outdated; the numbers above were pulled directly from Parchment's live tool, not from secondary reporting.

**Note the apparent tension** between §2 (aggregate ranking, Harvard outside top 20) and §4 (Harvard beats Stanford head-to-head, 65-35) — both can be true simultaneously if Harvard consistently loses to MIT/Caltech/Johns Hopkins-tier schools while still beating Stanford specifically; this is exactly the kind of nuance a single aggregate score collapses and a pairwise tool reveals. Don't treat the aggregate rank alone as a full picture of any one school's standing.

## 5. What this data can and can't tell you

- **Can:** tell you, for two specific schools a student is actually choosing between, which one most other admitted students picked — genuinely useful for a "which offer do I take" decision, and a real counterpoint to the "prestige" instinct (e.g. UCLA beating Berkeley 61-39 despite Berkeley's higher aggregate rank and reputation edge in some fields).
- **Can't:** tell you *why* — Parchment's data has no major/program breakdown, no financial-aid-adjusted comparison (a full-ride offer at School B will obviously beat a sticker-price admit to School A regardless of prestige, and this data can't separate that out), and an unknown, likely non-random sample (users of Parchment's specific transcript service, not all admitted students nationally).
- **Sample size matters a lot at the low end** — Caltech's #2 ranking (2022 edition) rests on just 435 matchups, versus Michigan's 28,304; a school with a small matchup count is a much noisier estimate than the confidence intervals in §4 might suggest at a glance.

---

*Companion files: `School Admissions Data Reference (CDS + IPEDS).md` (admit-rate/yield data this file's revealed-preference numbers should be read alongside — a school can have a high admit rate and still win head-to-head matchups, or vice versa), `Admissions Office Blogs & Podcasts Insights.md` and `MIT Admissions Blog Insights & Process Guide.md` (the "match, not prestige" advice this file's market data is a real-world counterpoint to), `NACAC State of College Admission Data.md` (the other cross-institutional aggregate data source in this project).*
