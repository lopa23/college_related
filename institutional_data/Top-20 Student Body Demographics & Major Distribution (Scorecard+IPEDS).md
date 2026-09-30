# Top-20 Student Body Demographics & Major Distribution (College Scorecard / IPEDS)

> **What this file is:** A federal-data answer to "who attends top-20 schools and what do their profiles look like" — built from the U.S. Department of Education's **College Scorecard API** (itself sourced from IPEDS, the same federal survey system underlying `School Admissions Data Reference (CDS + IPEDS).md`). Covers a **complete 20-school top tier**; all figures are institution-wide aggregates, not individual profiles, since no source in this file identifies individual students.
>
> **Why this file exists instead of a LinkedIn crawl:** the original ask was to characterize who attends top-20 schools by crawling LinkedIn profiles. LinkedIn's Alumni tool is login-walled (confirmed by testing it directly) and its User Agreement prohibits scraping; building a crawler would risk the account used and cross into unconsented bulk collection of identifiable students' data. This file gets at the same underlying question — class composition and major distribution — using aggregate federal data instead, which is public, authoritative, and carries no such risk.
>
> **Build script:** `pipeline/../institutional_data/school_data/fetch_scorecard_demographics_retry.py` (and its non-retry predecessor `fetch_scorecard_demographics.py`); raw output in `school_data/scorecard_demographics_top20.json`. Uses the same College Scorecard API (`api.data.gov/ed/collegescorecard/v1`) as `College Scorecard Field-of-Study Earnings (CS & Engineering).md`, with a broader field set (race/ethnicity, gender, first-gen, Pell, major/CIP-category percentages).

---

## 1. Demographics and major distribution, all 20 schools

All percentages are of total enrolled undergraduates (fall cohort, most recent Scorecard data year, typically 2022-23). "First-gen" and "Pell" are federal financial-aid-derived proxies, not self-identification surveys. Major percentages are broad CIP (Classification of Instructional Programs) 2-digit categories, not exact majors — e.g. "CS" bundles computer science with related computing fields, "Soc Sci" bundles economics, political science, sociology, etc.

| School | Size | Admit % | Women | Asian | White | Hisp/Latino | Black | Intl | 2+ races | First-gen | Pell | CS | Eng | Bio | Soc Sci |
|:--|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Princeton University | 5709 | 4.6% | 50.4% | 23.4% | 33.7% | 10.1% | 8.7% | 12.6% | 7.2% | 27.7% | 19.2% | 14.5% | 18.0% | 9.5% | 19.8% |
| MIT | 4535 | 4.5% | 48.2% | 35.2% | 21.3% | 14.1% | 7.7% | 11.7% | 6.8% | 25.9% | 19.3% | 35.2% | 27.3% | 4.1% | 0.8% |
| Harvard University | 7601 | 3.6% | 53.8% | 22.4% | 30.9% | 11.9% | 8.9% | 14.6% | 7.4% | 25.7% | 16.4% | 10.3% | 4.2% | 12.8% | 27.3% |
| Stanford University | 7554 | 3.6% | 51.6% | 28.7% | 23.0% | 17.1% | 7.4% | 12.8% | 9.6% | 30.3% | 19.2% | 21.1% | 14.8% | 3.4% | 15.0% |
| Yale University | 6758 | 3.9% | 51.5% | 21.9% | 31.2% | 16.6% | 9.3% | 11.2% | 7.1% | 25.0% | 20.4% | 9.2% | 5.1% | 11.0% | 22.6% |
| University of Pennsylvania | 10650 | 5.4% | 55.0% | 28.4% | 27.4% | 11.3% | 9.0% | 12.6% | 5.3% | 18.8% | 16.5% | 7.3% | 7.0% | 10.2% | 11.5% |
| Caltech | 987 | 2.6% | 45.2% | 35.9% | 18.7% | 17.4% | 4.7% | 14.1% | 8.9% | n/a | 18.0% | 35.2% | 28.4% | 8.0% | 0.0% |
| Duke University | 6442 | 5.7% | 53.7% | 21.8% | 35.2% | 10.7% | 8.7% | 10.5% | 7.4% | 13.5% | 14.0% | 10.8% | 15.0% | 11.7% | 14.0% |
| Brown University | 7226 | 5.4% | 50.0% | 22.9% | 32.9% | 12.1% | 8.2% | 12.7% | 7.9% | 17.0% | 13.8% | 15.8% | 4.7% | 12.3% | 25.3% |
| Johns Hopkins University | 5693 | 6.4% | 54.9% | 29.4% | 19.5% | 18.7% | 8.3% | 15.2% | 6.6% | 13.1% | 19.5% | 10.5% | 20.3% | 23.2% | 10.5% |
| Northwestern University | 9201 | 7.7% | 54.3% | 21.2% | 30.6% | 15.8% | 8.4% | 11.6% | 7.9% | 15.2% | 18.6% | 10.5% | 13.6% | 9.9% | 16.1% |
| Columbia University | 8973 | 4.0% | 49.8% | 18.7% | 28.7% | 15.4% | 7.5% | 19.7% | 6.2% | 25.0% | 22.7% | 16.0% | 12.1% | 7.2% | 26.9% |
| Cornell University | 15995 | 8.8% | 54.6% | 26.8% | 31.0% | 13.2% | 6.8% | 9.6% | 5.9% | 15.4% | 18.4% | 18.8% | 14.8% | 9.9% | 7.8% |
| University of Chicago | 7569 | 4.5% | 45.8% | 19.3% | 29.5% | 16.9% | 6.9% | 17.6% | 7.0% | 20.2% | 15.3% | 8.3% | 2.2% | 7.9% | 40.0% |
| UC Los Angeles | 33475 | 9.0% | 60.4% | 29.5% | 23.9% | 24.2% | 3.4% | 7.7% | 7.8% | 38.1% | 28.2% | 3.9% | 7.4% | 16.9% | 24.7% |
| UC Berkeley | 33068 | 11.0% | 55.8% | 35.4% | 19.8% | 22.1% | 2.1% | 9.8% | 6.8% | 34.6% | 28.6% | 19.1% | 11.1% | 9.2% | 16.5% |
| Rice University | 4776 | 8.0% | 49.6% | 29.1% | 25.6% | 16.7% | 7.9% | 12.8% | 5.5% | 14.5% | 17.0% | 14.6% | 15.6% | 16.1% | 9.8% |
| University of Notre Dame | 8818 | 11.3% | 48.7% | 5.7% | 59.4% | 15.3% | 4.7% | 6.9% | 5.6% | 10.2% | 13.7% | 6.6% | 15.2% | 12.0% | 13.7% |
| Vanderbilt University | 7208 | 5.9% | 52.5% | 18.6% | 39.1% | 11.4% | 9.2% | 11.2% | 5.7% | 12.2% | 20.2% | 9.3% | 12.2% | 6.6% | 30.9% |
| University of Michigan | 34177 | 15.6% | 53.9% | 18.5% | 46.7% | 11.7% | 5.2% | 7.6% | 5.7% | 20.6% | 18.1% | 16.0% | 13.9% | 9.6% | 10.9% |

*"Size" is total enrolled students (Scorecard's `student.size` field, which includes graduate students at research universities with large grad populations — Columbia's and Cornell's figures in particular are not undergraduate-only counts; treat as a rough institutional-scale indicator, not an undergraduate class size.)*

## 2. Patterns across the set

- **Race/ethnicity spread is wide, not uniform.** Asian enrollment share ranges from Notre Dame's 5.7% to Caltech's 35.9% and MIT's 35.2% — the two most STEM-concentrated schools in the set have by far the highest Asian enrollment shares, consistent with well-documented national patterns in STEM-heavy admissions pools. White enrollment share ranges from Johns Hopkins' 19.5% to Notre Dame's 59.4%, the widest spread of any category — Notre Dame is a clear outlier among this set on this dimension; Michigan (46.7%) and Vanderbilt (39.1%) sit closer to Notre Dame's end of the range than most of the other private schools.
- **International students range roughly 7-20%.** Columbia (19.7%) and Chicago (17.6%) have the highest international shares in this set; Notre Dame (6.9%) and Michigan (7.6%) the lowest. This roughly tracks each school's stated financial-aid posture toward international applicants (see `School Admissions Data Reference (CDS + IPEDS).md` and round 7's international-admissions coverage in `qualitative_insights/YouTube College Counseling Video Insights.md` §6f-h) — schools further from need-blind international aid tend to enroll fewer international students.
- **First-generation share varies more than any other single metric** — from Notre Dame's 10.2% and Vanderbilt's 12.2% up to UCLA's 38.1% and UC Berkeley's 34.6%. The two UCs are dramatic outliers on this metric within the set, consistent with California's large public-school pipeline and the UC system's stated commitment to first-gen access (see the UC-specific data already in `School Admissions Data Reference (CDS + IPEDS).md` §4a). Michigan's 20.6%, despite also being a large public flagship, sits much closer to the private-school range than to Berkeley/UCLA — a reminder that "public" alone doesn't predict first-gen share.
- **Pell Grant recipient share (a low-income proxy) shows the same UC-outlier pattern**: UCLA (28.2%) and Berkeley (28.6%) roughly double most of the private schools in the set (Notre Dame 13.7%, Brown 13.8%, Duke 14.0% are the lowest). Michigan (18.1%) again lands mid-pack rather than near its fellow public flagships.
- **Gender skews female almost everywhere**, consistent with the national undergraduate gender gap — the exceptions are the most STEM-concentrated schools: Caltech (45.2% women) and UChicago (45.8%, though Chicago is not STEM-concentrated the way Caltech is, so this may reflect a different dynamic) are the only two under 50%. MIT (48.2%) is close to parity despite its STEM concentration; Vanderbilt (52.5%) and Michigan (53.9%) both skew clearly female.
- **Major distribution splits into two clear clusters.** Caltech and MIT are outliers with 35%+ in CS alone and 60%+ combined CS+Engineering, leaving under 5% combined for biological sciences and social science at both. Every other school in the set spreads more evenly across CS, engineering, biological sciences, and social sciences, with UChicago (40.0%), Vanderbilt (30.9%) and Harvard (27.3%) the most social-science-concentrated of the group.
- **Michigan is the only school in the set with a meaningfully diversified major mix into business (7.5%) and health (3.9%)** — every other school reports 0% in one or both categories. As the largest and most comprehensive institution in this set (34,177 total enrolled, more than double the next-largest), Michigan's undergraduate business school and health-sciences programs show up in the aggregate mix in a way no other school here has; it's also the least selective by admit rate in the set (15.6%, vs. the next-highest Notre Dame at 11.3%).

## 3. What this can and can't tell you

- **This is class-wide composition, not individual profiles.** It answers "what does the class as a whole look like," not "what does a typical admitted student's resume look like" — for the latter, this project's `applicant_profiles/combined_profiles.json` archive (real self-reported Reddit/College Confidential profiles) is the better source, and the FERPA file-review findings in `qualitative_insights/YouTube College Counseling Video Insights.md` §6d-a/§6e-a/§6h are the closest thing to real individual admitted-student data anywhere in this project.
- **Race/ethnicity categories are IPEDS-defined**, not self-identification in the fuller sense some students would use (e.g., no sub-Asian or sub-Hispanic breakdowns, "two or more races" and "unknown" are separate catch-all buckets).
- **No geographic-origin (state/country of residence) data is included here.** College Scorecard's public API doesn't expose per-school state-of-origin counts the way LinkedIn's Alumni tool would show "where they're from"; that data exists in IPEDS' separate "Residence and Migration" survey component but would require a dedicated pull beyond this file's scope — flag if this is wanted as a follow-up.
- **Major percentages are class-wide, not by graduating cohort or by year**, so they reflect current enrollment mix across all class years, not incoming first-years specifically.

---

*Companion files: `School Admissions Data Reference (CDS + IPEDS).md` (admit rates, test ranges, CDS factor weightings for the same and additional schools), `College Scorecard Field-of-Study Earnings (CS & Engineering).md` (earnings by major for a CS/engineering-focused school set), `SFFA Lawsuit Data (Harvard & UNC).md` (disclosed race-conscious admissions data for two of these schools), `applicant_profiles/combined_profiles.json` (individual self-reported applicant profiles, the closer answer to "what do admitted students' profiles look like").*
