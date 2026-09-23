# NACAC State of College Admission Data

> **What this is:** Real, primary-sourced survey data from NACAC (National Association for College Admission Counseling), a professional association that periodically surveys its own member colleges on what factors actually drive admission decisions, plus IPEDS-derived fact sheets on acceptance rates, yield, and test-submission trends. NACAC discontinued its old single annual "State of College Admission" report/book (last full edition 2019) and redesigned it as a rolling series of topic-specific fact sheets published on nacacnet.org throughout the year. Everything below was read directly from NACAC's own official fact-sheet PDFs — real data tables with N counts and IPEDS/internal-survey sourcing, not secondhand paraphrase.
>
> **Why this belongs in this project:** every other qualitative-insight file in this folder (AMA testimony, admissions-office blogs, podcasts, webinars) is one school's or one practitioner's account. This is the one source in the whole set that's an actual **cross-institutional survey** — hundreds of colleges self-reporting what they weight, aggregated. It's the closest thing to ground truth for "how much does X actually matter, on average, across the industry" that exists publicly. It does not replace any single school's own stated policy (§4 of `School Admissions Data Reference (CDS + IPEDS).md`, or the CDS section-C7 factor ratings in §2 of the same file, remain the right source for a *specific* school) — it's the industry-wide baseline those school-specific sources should be read against.

---

## 1. Factors in the admission decision (Fall 2023 cycle, N=183–185 four-year colleges)

**Source:** "State of College Admission: Factors in the Admission Decision Fact Sheet," NACAC — [nacacnet.org/factors-in-the-admission-decision](https://www.nacacnet.org/factors-in-the-admission-decision/).

| Factor | Considerable importance | Moderate | Limited | None |
|:--|--:|--:|--:|--:|
| HS grades, college prep courses | 76.8% | 15.1% | 4.9% | 3.2% |
| Total HS grades (all courses) | 74.1% | 18.9% | 5.4% | 1.6% |
| Strength of HS curriculum | 63.8% | 22.7% | 10.3% | 3.2% |
| Positive character attributes | 28.3% | 37.5% | 18.5% | 15.8% |
| Essay/writing sample | 18.9% | 37.3% | 26.5% | 17.3% |
| Student's interest in attending (demonstrated interest) | 15.7% | 27.6% | 25.4% | 31.4% |
| Counselor recommendation | 11.9% | 40.0% | 27.6% | 20.5% |
| Teacher recommendation | 10.8% | 40.5% | 28.1% | 20.5% |
| Extracurricular activities | 6.5% | 44.3% | 30.8% | 18.4% |
| HS class rank | 5.5% | 22.4% | 43.2% | 29.0% |
| Admission test scores (ACT/SAT) | 4.9% | 25.4% | 38.9% | 30.8% |
| Portfolio | 4.9% | 10.8% | 24.3% | 60.0% |
| Interview | 4.3% | 8.6% | 32.4% | 54.6% |
| Work experience | 2.2% | 30.8% | 40.0% | 27.0% |
| State graduation exam scores | 1.6% | 6.5% | 18.4% | 73.5% |
| Subject test scores (AP/IB) | 1.1% | 22.2% | 25.9% | 50.8% |

**How to read this against the qualitative files:** the ranking here — grades/curriculum strength dominate, essay and demonstrated interest are solidly mid-tier, class rank/test scores/interview are low, legacy and ability-to-pay are near the bottom — matches almost exactly what the AMA file's JeLev (a ~50%-admit research LAC) and Penn's official AMA team independently said in their own words. This table is the reason those individual claims generalize reasonably well: they're not outliers, they're closely tracking the actual 185-college average.

## 2. The test-score collapse — the single most striking trend in this dataset

**% of colleges rating admission test scores (ACT/SAT) as "considerable importance," by year:**

| 2012 | 2013 | 2014 | 2016 | 2017 | 2018 | 2023 |
|--:|--:|--:|--:|--:|--:|--:|
| 56% | 58% | 56% | 54% | 52% | 46% | **5%** |

(No data collected 2019–2022.) Test scores went from being rated "considerable importance" by a majority of colleges throughout the 2010s to essentially falling off a cliff by fall 2023 — a collapse of over 40 percentage points, driven by widespread test-optional adoption. For comparison, over the same span:

| Factor | 2012 | 2018 | 2023 | Direction |
|:--|--:|--:|--:|:--|
| HS grades, college prep | 82% | 73% | 77% | Roughly flat |
| Strength of curriculum | 65% | 62% | 64% | Roughly flat |
| Essay/writing sample | 20% | 23% | 19% | Roughly flat |
| Demonstrated interest | 18% | 16% | 16% | Roughly flat |
| HS class rank | 13% | 9% | 5% | Declining |
| Subject test scores (AP/IB) | 5% | 6% | 1% | Collapsed, same pattern as ACT/SAT |

**This directly corroborates and quantifies a theme already documented qualitatively elsewhere in this project** — MIT's Dean Schmill's 2022 post (in `MIT Admissions Blog Insights & Process Guide.md` §3) explicitly frames MIT's decision to *reinstate* testing as a deliberate outlier move against this exact industry trend, and Yale's podcast (`Admissions Office Blogs & Podcasts Insights.md` §3) independently describes testing as minor relative to transcript/essay weight — both individual claims now sit against a real, quantified, 185-college baseline instead of standing alone.

**Corroborating data point — actual test *submission* rates (not importance ratings), IPEDS-derived, Fall 2017–2021, across 1,532 four-year non-open-admission colleges:**

| | Fall 2017 | Fall 2021 |
|:--|--:|--:|
| % of enrollees submitting ACT | 58% | 31% |
| % of enrollees submitting SAT | 46% | 24% |

Public institutions retained meaningfully higher submission rates than private institutions throughout — worth remembering when reading any single school's SAT-submission-rate figure in §1 of `School Admissions Data Reference (CDS + IPEDS).md` against this national baseline.

## 3. Student characteristics — how much they matter, Fall 2023 (same fact sheet)

| Characteristic | Considerable | Moderate | Limited | No influence |
|:--|--:|--:|--:|--:|
| First-generation status | 7.0% | 9.7% | 28.1% | 55.1% |
| State/country of residence | 7.0% | 9.7% | 28.1% | 55.1% |
| Gender | 2.8% | 9.4% | 12.8% | 75.0% |
| High school attended | 1.6% | 17.8% | 34.1% | 46.5% |
| Ability to pay | 1.6% | 7.6% | 13.0% | 77.8% |
| Alumni relations (legacy) | 0.5% | 3.8% | 30.3% | 65.4% |

**A necessary caveat NACAC itself does not fully resolve:** self-reported legacy and ability-to-pay figures here are low, but this 185-college sample is dominated by the broad national pool of four-year colleges, most of which don't practice legacy preference at all. It's near-certain these self-reported averages substantially understate real-world influence at the small number of highly selective schools that *do* weight legacy heavily — see `SFFA Lawsuit Data (Harvard & UNC).md` §2 for Harvard's own disclosed data showing legacy applicants admitted at ~33-34%, roughly 5x-plus the non-legacy rate, a sharp contrast with this survey's near-zero average. Read this table as "typical college," not as evidence about elite-school practice specifically.

## 4. Acceptance rate and yield trends, national (IPEDS-derived fact sheets)

**Selectivity** — [nacacnet.org/selectivity-acceptance-rates-at-4-year-colleges](https://www.nacacnet.org/selectivity-acceptance-rates-at-4-year-colleges/):

| | 2014 | 2019 | 2020 | 2021 | 2022 |
|:--|--:|--:|--:|--:|--:|
| Average acceptance rate, all 4-yr colleges | — | 68% | 70% | 73.1% | 72.6% |
| Public colleges | 68% | — | — | — | 78% |
| Private colleges | — | — | — | — | 70% |

Fall 2022: average applicants per institution 8,029 (public 14,263, private 4,972); 1,013 colleges had acceptance rates of 71% or higher. Public-college acceptance rates rose 10 points from 2014 to 2022 (68%→78%); private colleges rose only about 5 points over the same span.

**Yield:**

| | 2014 | 2016 | 2022 |
|:--|--:|--:|--:|
| Average yield rate, all 4-yr colleges | 36% | — | 30% |
| Public colleges | 36.9% | — | 25.3% |
| Private colleges | 36.0% | — | 32.6% |

Public-college yield fell more sharply than private since 2016 — a genuine structural shift, not just noise, and worth reading alongside §6 of `School Admissions Data Reference (CDS + IPEDS).md`'s ten-year admit-rate trend data, which shows several large publics (Minnesota, Ohio State, Buffalo) becoming *less* selective over the same period — rising acceptance and falling yield at public institutions nationally are two views of the same broader dynamic.

**This national trend directly matches the archive's own findings**: the 60-school admit-rate trend in `School Admissions Data Reference (CDS + IPEDS).md` §6 found a cluster of publics (Minnesota, RPI, Rose-Hulman, Buffalo) getting easier to get into over the same decade — this NACAC data confirms that's not an artifact of the 60-school sample, but part of a real national pattern of public institutions loosening as demand softened relative to private institutions.

## 5. A separate survey — do not conflate with the institutional data above

NACAC also published the **"NACAC College Admission Process Survey"** (August 2023), conducted by The Harris Poll and funded by the Lumina Foundation. This is a **fundamentally different kind of data**: opinion polling of 1,010 young adults ages 16–22 (Feb–Mar 2023, ±4.0 points at 95% confidence) about their *perceptions* of what matters in admissions — not colleges self-reporting their own actual weighting. It found 57% of respondents named "grades in all courses" and 56% named "admission test scores" among their top-5 guessed factors — **these are student guesses**, notably an overestimate of test-score importance relative to the actual 4.9% "considerable importance" institutional figure in §1 above, a real and interesting gap between perception and practice, but it should never be cited as if it were institutional data. [PDF](https://www.nacacnet.org/wp-content/uploads/NACAC-College-Admission-Process-Research_FINAL.pdf)

## 6. What wasn't found

No first-year retention or admissions-office staffing fact sheets were located in this research pass — NACAC's site structure suggests these may exist as membership-login-gated dashboard content, or may not yet be published in the redesigned fact-sheet series. If retention/staffing data is needed later, that's the specific gap to chase.

---

*Companion files: `School Admissions Data Reference (CDS + IPEDS).md` (school-specific CDS factor ratings and admit-rate trends this file's national averages should be read against), `SFFA Lawsuit Data (Harvard & UNC).md` (the elite-school legacy data that contradicts this survey's near-zero national legacy average), `Admissions Officer AMA Insights & Profile Query Guide.md` and `Admissions Office Blogs & Podcasts Insights.md` (individual practitioner claims this survey provides an industry-wide baseline for).*
