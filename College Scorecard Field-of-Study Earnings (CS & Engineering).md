# College Scorecard Field-of-Study Earnings (CS & Engineering)

> **What this is:** Federal earnings data broken down by **major**, not just by institution — the College Scorecard's "Field of Study" file, a separate dataset from the school-level Scorecard numbers already in `school_facts.json`. Every earnings figure elsewhere in this project (§3 of `School Admissions Data Reference (CDS + IPEDS).md`) is a whole-institution median across every graduate of every major. This file answers a different, more specific question: **what does a Computer Science or Engineering graduate specifically earn from School X**, which can diverge sharply from that school's overall figure. Source: [College Scorecard "Most Recent Cohorts: Field of Study" bulk data file](https://collegescorecard.ed.gov/data/), downloaded directly (17MB zip, 227,981 rows covering every institution/major/credential-level combination nationally). Machine-readable: `school_data/field_of_study/national_cs_engineering_earnings.csv` (bachelor's-level only, CIP codes 11.xxxx Computer/Information Sciences and 14.xxxx Engineering, ~6,500 rows) and the original `Field-of-Study.zip`.
>
> **Methodology note:** "1-year earnings" and "2-year earnings" are median earnings of graduates working and not enrolled, measured 1 and 2 years after completion, for the cohort with the highest-earning outcomes reported (`_HI_` fields) — this is the Scorecard's own standard field-of-study earnings measure. Figures marked "PS" in the raw data (privacy-suppressed, small cohorts) are excluded rather than treated as zero. `CIPCODE` `1107` = "Computer Science" specifically; `1101` = "Computer and Information Sciences, General," a broader/different major bucket some schools also report separately — several schools below appear twice for this reason, and the two numbers can differ substantially within the same school.

---

## 1. Top CS/Engineering bachelor's programs nationally by 1-year earnings (n≥30 graduates)

| Institution | Program | Median earnings, 1yr out | n |
|:--|:--|--:|--:|
| Carnegie Mellon University | Computer Science | $161,723 | 97 |
| Harvard University | Computer Science | $140,072 | 58 |
| University of Washington (Seattle/Bothell/Tacoma) | Computer Engineering | $137,584 | 33 |
| Stanford University | Computer Science | $136,126 | 96 |
| Brown University | Computer Science | $130,101 | 95 |
| Cornell University | Computer Science | $127,764 | 228 |
| UC Berkeley | Electrical, Electronics, and Communications Eng. | $126,367 | 182 |
| UC Berkeley | Computer Science | $125,250 | 313 |
| Princeton University | Computer Engineering | $122,809 | 41 |
| Rice University | Computer and Information Sciences | $122,770 | 50 |
| MIT | Computer Science | $118,191 | 134 |
| UCLA | Computer and Information Sciences | $117,100 | 117 |
| Carnegie Mellon University | Electrical, Electronics, and Communications Eng. | $116,935 | 62 |

**CMU's Computer Science program tops every school in this dataset, including Harvard, Stanford, and MIT** — a genuinely new finding not visible anywhere else in this project. This is consistent with (and now quantifies) the pattern already established in `School Admissions Data Reference (CDS + IPEDS).md` §4b: CMU's SCS is described there as the most selective single program found in this whole project's admissions data, and here it's also the highest-earning.

## 2. The 60-school curated list, Computer Science-coded rows only, sorted by 1-year earnings

| School | 1-yr median earnings | Median debt | n |
|:--|--:|--:|--:|
| Carnegie Mellon University | $161,723 | $21,442 | 97 |
| Harvard University | $140,072 | $0 | 58 |
| Stanford University | $136,126 | $10,399 | 96 |
| Yale University | $133,998 | $12,750 | 24 |
| Brown University | $130,101 | $11,500 | 95 |
| California Institute of Technology | $129,693 | $0 | 29 |
| Cornell University | $127,764 | $14,698 | 228 |
| University of Pennsylvania | $127,623 | $13,500 | 16 |
| UC Berkeley | $125,250 | $13,900 | 313 |
| Harvey Mudd College | $123,339 | $22,949 | 26 |
| Rice University | $122,770 | $12,381 | 50 |
| MIT | $118,191 | $12,000 | 134 |
| UCLA | $117,100 | $15,248 | 117 |
| Duke University | $115,135 | $13,500 | 141 |
| Dartmouth College | $111,259 | $18,490 | 63 |
| Columbia University | $108,903 | $20,397 | 118 |
| Johns Hopkins University | $105,950 | $12,750 | 48 |
| University of Southern California | $104,298 | $20,178 | 117 |
| Vanderbilt University | $101,714 | $14,500 | 48 |
| University of Washington | $101,710 | $16,118 | 236 |
| University of Illinois Urbana-Champaign | $101,262 | $20,500 | 151 |
| University of Michigan | $100,643 | $20,000 | 539 |
| Swarthmore College | $97,897 | $0 | 31 |
| Tufts University | $96,349 | $15,500 | 97 |
| Northeastern University | $95,288 | $23,001 | 188 |
| University of Chicago | $93,918 | $0 | 39 |
| Georgetown University | $93,493 | $16,007 | 26 |
| Washington University in St. Louis | $89,930 | $15,500 | 53 |
| Georgia Institute of Technology | $89,428 | $21,125 | 397 |
| University of Texas at Austin | $89,133 | $20,500 | 378 |
| UC San Diego | $87,738 | $16,550 | 521 |
| Worcester Polytechnic Institute | $86,601 | $27,000 | 140 |
| UC Santa Barbara | $86,276 | $11,000 | 80 |
| University of Maryland, College Park | $84,727 | $0 | 367 |
| University of Rochester | $84,531 | $19,000 | 71 |
| Northwestern University | $84,037 | $14,600 | 46 |
| Rensselaer Polytechnic Institute | $83,880 | $23,250 | 231 |
| University of Virginia | $83,639 | $17,783 | 194 |
| Virginia Tech | $82,448 | $20,500 | 205 |
| Boston University | $82,237 | $23,250 | 135 |
| Purdue University | $81,749 | $19,375 | 174 |
| University of Notre Dame | $80,593 | $19,000 | 96 |
| Rose-Hulman Institute of Technology | $77,382 | $24,500 | 52 |
| University of Florida | $76,677 | $16,000 | 169 |
| UC Davis | $76,488 | $14,282 | 291 |
| Texas A&M University | $76,419 | $20,187 | 91 |
| New York University | $75,653 | $19,734 | 277 |
| University of North Carolina at Chapel Hill | $74,162 | $14,131 | 233 |
| Case Western Reserve University | $74,006 | $25,391 | 75 |
| Pennsylvania State University | $73,647 | $26,000 | 182 |
| Emory University | $73,250 | $15,250 | 33 |
| University of Wisconsin-Madison | $72,878 | $22,500 | 205 |
| UC Irvine | $70,796 | $15,500 | 505 |
| Wake Forest University | $70,098 | $20,674 | 29 |
| Rutgers University | $69,934 | $21,500 | 478 |
| University of Minnesota | $69,239 | $19,500 | 325 |
| Ohio State University | $68,553 | $23,000 | 69 |
| University at Buffalo | $60,109 | $20,500 | 145 |

*(Where a school reports both a "Computer Science" and a separate "Computer and Information Sciences, General" row, the higher-earnings row is shown above for readability; both rows are in the underlying CSV. Two of the 60 curated schools had no CS earnings data reported — likely small/suppressed cohorts.)*

## 3. What this reveals that the rest of the archive doesn't

- **A school's overall earnings figure (§3 of the main reference doc) can meaningfully understate or overstate its CS program's specific outcome.** Georgia Tech, UT Austin, and UC San Diego all sit in the high-$80Ks/high-$70Ks for CS specifically — solid, but well below the CMU/Harvard/Stanford tier, despite Georgia Tech's overall institutional earnings figure (§3, $102,772) actually being *higher* than several schools whose CS-specific number beats it here. Major-level and institution-level rankings are genuinely different rankings, not just noisier versions of each other.
- **Debt and earnings don't move together in a simple way.** Several elite schools show $0 median debt for CS (Harvard, Caltech, Swarthmore, Chicago, Maryland) alongside high earnings — likely reflecting strong need-based aid and a student population with low borrowing need — while some upper-tier-but-not-elite schools (Rose-Hulman, Penn State, Northeastern, RPI, Case Western, WPI) show both moderate earnings *and* $20K+ median debt, a meaningfully worse combination than either extreme.
- **Sample size varies enormously and matters.** UC schools and large publics (Berkeley, UCSD, UC Irvine, Michigan, Rutgers) report n=300-500+, genuinely stable estimates; several elite privates (Yale n=24, Wake Forest n=29, Caltech n=29, Harvey Mudd n=26) rest on much smaller cohorts, where a handful of FAANG-vs-teaching-job outcomes could swing the median noticeably year to year.

## 4. Reading this against the admission-structure file

Cross-reference `School Admissions Data Reference (CDS + IPEDS).md` §4c (direct-admit vs. unified-declare structure): several of the highest-earning CS programs here (CMU, Berkeley EECS, Georgia Tech, UT Austin) are also **direct-admit or competitive-declare** schools — meaning the earnings premium documented here is specifically attached to *getting into the CS program itself*, not just the university generally, at exactly the schools where getting into the CS program is hardest. This is a real, quantified version of the qualitative point made throughout the admissions-blog files: "the campus-wide numbers overstate an applicant's chances of getting into CS specifically" — and now this file shows what's actually at stake in that gap.

---

*Companion files: `School Admissions Data Reference (CDS + IPEDS).md` §3 (whole-institution earnings, the figure this file's major-specific numbers should be read against) and §4c (admission-structure data explaining why several of the highest-earning programs here are also the hardest to get directly admitted to), `school_data/school_facts.json` (institution-level source data).*
