# School Admissions Data Reference (CDS + IPEDS)

> **What this is:** Official-source numbers (Common Data Set filings + federal IPEDS/NCES data) for 60 schools relevant to elite and CS/engineering admissions, to give the profile archive and the book/AMA files a real denominator. Machine-readable versions: `school_data/school_facts.json` (§1–3, latest year), `school_data/uc_by_discipline.json` (§4a, UC by campus/discipline/year), `school_data/school_admit_trends.json` (§6, 2014–2024 trend per school), and `school_data/ipeds_national/` (the full national IPEDS record, ~2,000 institutions, not just these 60 — see its own README for schema). A companion file, `SFFA Lawsuit Data (Harvard & UNC).md`, covers the one-time public disclosure of Harvard's and UNC's internal admissions data from *SFFA v. Harvard* / *SFFA v. UNC* — kept separate since it's a different kind of source (litigation record, not CDS/IPEDS) and needs its own confidence-labeling scheme.
>
> **Source & caveats:** Extracted by the open-source collegedata.fyi project from each school's own CDS (`cds_year` in the JSON says which year). Extraction is automated — some fields are missing or were withheld by that project as inconsistent (e.g. MIT's applicant/admit counts). Admit rate here is the IPEDS figure, in percent. **Verify any number against the school's own CDS before citing it.** SAT range is the sum of the reported section 25th/75th percentiles (an approximation of the composite range, not an official composite). C7 codes: **VI** Very Important · **I** Important · **C** Considered · **NC** Not Considered · — not reported.

## 1. Selectivity and test ranges (sorted most → least selective)

| School | Admit % | SAT (approx.) | ACT mid-50 | SAT submit % | ED admit % | Avg GPA (CDS) |
|:--|--:|:--|:--|--:|--:|--:|
| California Institute of Technology | 3 | 1530–1580 | 35–36 | — | — | — |
| Stanford University | 4 | 1510–1580 | 34–35 | 51 | — | 3.94 |
| Harvard University | 4 | 1510–1580 | 34–36 | 54 | — | 4.22 |
| Yale University | 4 | 1470–1570 | 33–35 | 61 | — | — |
| Columbia University | 4 | 1510–1580 | 34–35 | 45 | 13% | — |
| University of Chicago | 4 | 1510–1580 | 34–35 | 49 | — | 4.54 |
| Massachusetts Institute of Technology | 5 | 1520–1580 | 34–36 | 83 | — | — |
| Princeton University | 5 | 1510–1580 | 34–35 | 56 | — | 3.96 |
| University of Pennsylvania | 5 | 1510–1570 | 34–36 | 50 | — | 3.9 |
| Dartmouth College | 5 | 1500–1570 | 33–35 | 51 | 22% | — |
| Brown University | 5 | 1510–1580 | 34–35 | 61 | 18% | — |
| Northeastern University | 5 | 1440–1540 | 33–35 | 24 | 43% | — |
| Duke University | 6 | 1500–1570 | 34–35 | 48 | — | — |
| Johns Hopkins University | 6 | 1520–1570 | 34–36 | 50 | 11% | 3.93 |
| Vanderbilt University | 6 | 1500–1570 | 34–35 | 27 | 14% | 3.895 |
| Swarthmore | 7 | 1490–1560 | 33–35 | 39 | 18% | — |
| Northwestern University | 8 | 1510–1570 | 33–35 | 46 | 23% | — |
| Rice University | 8 | 1510–1570 | 34–35 | 48 | 11% | — |
| Cornell University | 9 | 1500–1570 | 33–35 | 40 | — | — |
| University of California, Los Angeles | 9 | 1300–1530 | 29–35 | 81 | — | 3.94 |
| New York University | 9 | 1480–1560 | 34–35 | 28 | — | — |
| University of Southern California | 10 | 1450–1550 | 32–35 | 34 | — | 3.85 |
| University of California, Berkeley | 11 | 1310–1530 | 30–35 | 82 | — | 3.9 |
| University of Notre Dame | 11 | 1455–1560 | 33–35 | 33 | — | — |
| Emory University | 11 | 1470–1550 | 32–35 | 43 | — | — |
| Boston University | 11 | 1420–1530 | 32–34 | 33 | 31% | 3.86 |
| Tufts University | 11 | 1470–1560 | 33–35 | 40 | — | — |
| Carnegie Mellon University | 12 | 1500–1570 | 34–35 | 53 | 21% | 3.89 |
| Washington University in St. Louis | 12 | 1500–1570 | 33–35 | 29 | 27% | — |
| Harvey Mudd College | 13 | 1500–1570 | 34–36 | 52 | 18% | — |
| Georgetown University | 13 | 1390–1550 | 31–35 | 78 | — | — |
| Georgia Institute of Technology | 14 | 1370–1540 | 30–34 | 77 | — | 4.17 |
| University of North Carolina at Chapel Hill | 15 | 1390–1530 | 28–34 | 28 | — | 4.47 |
| University of Michigan | 16 | 1360–1530 | 31–34 | 51 | — | 3.9 |
| University of Virginia | 17 | 1410–1540 | 32–35 | 46 | 28% | — |
| Wake Forest | 22 | 1410–1520 | 32–34 | 22 | — | — |
| University of Florida | 24 | 1320–1480 | 29–33 | 80 | — | 3.9 |
| Olin College | 25 | 1493–1558 | 34–35 | 25 | — | — |
| University of Texas at Austin | 27 | 1250–1510 | 27–33 | 56 | — | — |
| University of California, San Diego | 27 | 1270–1480 | 28–34 | 89 | — | 3.88 |
| University of California, Irvine | 29 | 1230–1430 | 26–33 | 91 | — | — |
| University of California, Santa Barbara | 33 | 1230–1460 | 28–34 | 82 | — | 4.29 |
| Case Western Reserve University | 37 | 1430–1540 | 32–34 | 46 | 25% | 3.78 |
| University of Washington | 39 | 1200–1453 | 27–33 | 81 | — | 3.835791 |
| University of Rochester | 40 | 1410–1540 | 31–34 | 19 | — | 3.72 |
| University of Illinois Urbana-Champaign | 42 | 1310–1520 | 30–34 | 48 | — | — |
| University of California, Davis | 42 | 1160–1400 | 25–33 | 90 | — | 4.04 |
| University of Wisconsin-Madison | 45 | 1380–1520 | 29–33 | 15 | — | 3.91 |
| University of Maryland, College Park | 45 | 1400–1530 | 32–35 | 42 | — | — |
| Purdue University | 50 | 1200–1480 | 27–34 | 79 | — | — |
| Virginia Tech | 55 | 1280–1450 | 28–32 | 41 | — | 4.09 |
| Texas A&M University | 57 | 1150–1400 | 25–31 | 79 | — | — |
| Rutgers University | 58 | 1310–1500 | 28–33 | 50 | — | — |
| Worcester Polytechnic Institute | 60 | — | — | — | 19% | — |
| Ohio State University | 61 | 1310–1480 | 28–32 | 17 | — | — |
| Penn State | 61 | 1240–1420 | 27–32 | 31 | — | 3.67 |
| Rensselaer Polytechnic Institute | 63 | 1375–1510 | 30–34 | 49 | 58% | 3.8 |
| University at Buffalo | 74 | 1210–1380 | 27–32 | 28 | — | 3.7 |
| Rose-Hulman | 77 | 1320–1500 | 29–34 | 53 | — | 3.83 |
| University of Minnesota | 80 | 1300–1500 | 26–31 | 8 | — | — |

## 2. How schools say they weigh factors (CDS section C7)

| School | Rigor | GPA | Tests | Essay | Recs | ECs | Talent | Character | First-gen | Legacy | Dem. interest |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| California Institute of Technology | VI | VI | VI | VI | VI | VI | VI | VI | VI | VI | VI |
| Stanford University | VI | VI | VI | VI | VI | VI | VI | VI | C | C | NC |
| Harvard University | C | C | C | C | C | C | C | C | C | C | NC |
| Yale University | VI | VI | C | VI | VI | VI | VI | VI | C | C | NC |
| Columbia University | VI | VI | C | VI | VI | VI | I | VI | C | C | NC |
| University of Chicago | VI | C | C | VI | VI | VI | VI | VI | C | — | — |
| Massachusetts Institute of Technology | I | I | I | I | I | I | I | VI | C | NC | NC |
| Princeton University | VI | VI | VI | VI | VI | VI | VI | VI | C | C | NC |
| University of Pennsylvania | VI | VI | C | VI | VI | I | I | VI | C | C | NC |
| Dartmouth College | VI | VI | VI | VI | VI | VI | I | VI | C | C | C |
| Brown University | VI | VI | VI | VI | VI | I | VI | VI | C | C | NC |
| Northeastern University | VI | VI | VI | C | VI | I | I | I | C | NC | C |
| Duke University | VI | VI | C | C | VI | VI | VI | VI | C | C | C |
| Johns Hopkins University | VI | VI | VI | VI | VI | I | I | I | C | NC | NC |
| Swarthmore | VI | VI | C | VI | VI | C | C | VI | C | C | NC |
| Northwestern University | VI | VI | VI | VI | VI | VI | VI | VI | VI | VI | VI |
| Rice University | VI | VI | VI | VI | VI | VI | VI | VI | C | C | C |
| University of California, Los Angeles | VI | VI | NC | VI | NC | I | I | I | C | NC | NC |
| New York University | — | — | — | VI | — | — | — | — | — | — | — |
| University of Southern California | VI | VI | C | VI | VI | I | I | VI | C | C | NC |
| University of Notre Dame | VI | VI | I | VI | VI | — | VI | VI | I | C | — |
| Emory University | VI | VI | I | I | VI | VI | VI | VI | C | — | — |
| Boston University | VI | VI | C | I | I | I | NC | I | C | NC | C |
| Tufts University | VI | VI | VI | VI | VI | VI | VI | VI | VI | VI | VI |
| Carnegie Mellon University | VI | VI | C | I | I | VI | I | VI | I | NC | NC |
| Washington University in St. Louis | VI | VI | VI | VI | VI | — | VI | VI | I | C | C |
| Harvey Mudd College | VI | VI | C | I | VI | I | C | I | C | NC | NC |
| Georgetown University | VI | VI | VI | VI | VI | I | VI | VI | — | — | — |
| Georgia Institute of Technology | VI | VI | C | I | C | I | C | VI | NC | NC | NC |
| University of North Carolina at Chapel Hill | VI | I | C | VI | VI | VI | VI | VI | C | C | NC |
| University of Michigan | VI | VI | VI | VI | VI | VI | VI | VI | VI | VI | VI |
| University of Virginia | VI | VI | C | I | I | I | I | VI | C | NC | NC |
| Wake Forest | VI | VI | C | VI | I | I | I | VI | C | C | C |
| University of Florida | VI | VI | I | I | NC | VI | VI | I | C | NC | NC |
| University of Texas at Austin | C | C | C | C | C | C | C | C | C | NC | NC |
| University of California, San Diego | VI | VI | NC | VI | NC | I | I | I | C | NC | NC |
| University of California, Irvine | VI | VI | NC | VI | NC | VI | VI | I | C | NC | NC |
| University of California, Santa Barbara | I | VI | NC | VI | NC | C | C | C | C | NC | NC |
| Case Western Reserve University | VI | VI | C | I | I | VI | I | I | C | C | C |
| University of Washington | VI | VI | NC | VI | NC | I | I | C | I | NC | NC |
| University of Rochester | VI | VI | C | I | I | VI | I | VI | C | C | I |
| University of Illinois Urbana-Champaign | VI | VI | C | I | NC | I | I | I | I | NC | NC |
| University of California, Davis | VI | VI | NC | I | NC | I | I | I | C | NC | NC |
| Purdue University | — | — | — | — | — | VI | — | — | — | — | — |
| Virginia Tech | VI | VI | C | VI | NC | C | C | C | VI | NC | NC |
| Texas A&M University | VI | VI | C | I | C | VI | VI | C | I | NC | — |
| Worcester Polytechnic Institute | VI | VI | C | VI | — | I | I | — | C | C | — |
| Rensselaer Polytechnic Institute | VI | VI | C | I | I | I | C | I | C | C | C |
| University of Minnesota | VI | VI | VI | VI | VI | VI | VI | VI | VI | VI | VI |

## 3. Cost and outcomes (federal data)

| School | Avg net price | Net price, income <$30k | 6-yr grad rate | Median earnings 10 yr | Median debt |
|:--|--:|--:|--:|--:|--:|
| California Institute of Technology | $16,075 | $-2,133 | 94% | $128,566 | — |
| Stanford University | $13,807 | $-2,536 | 92% | $124,080 | $12,000 |
| Harvard University | $19,066 | $8,697 | 98% | $101,817 | $14,000 |
| Yale University | $23,777 | $17,633 | 96% | $100,533 | $12,975 |
| Columbia University | $21,590 | $4,570 | 96% | $102,491 | $21,500 |
| University of Chicago | $14,860 | $-1,264 | 96% | $91,885 | $15,000 |
| Massachusetts Institute of Technology | $20,111 | $-2,533 | 96% | $143,372 | $14,768 |
| Princeton University | $6,128 | $41 | 98% | $110,066 | $10,320 |
| University of Pennsylvania | $28,699 | $-3,012 | 97% | $111,371 | $15,715 |
| Dartmouth College | $29,519 | $41 | 96% | $97,434 | $17,500 |
| Brown University | $25,184 | $-420 | 96% | $93,487 | $11,428 |
| Northeastern University | $30,915 | $2,264 | 91% | $92,538 | $24,250 |
| Duke University | $29,612 | $735 | 97% | $97,800 | $13,000 |
| Johns Hopkins University | $18,809 | $428 | 94% | $87,555 | $10,250 |
| Vanderbilt University | $15,846 | $3,414 | 94% | $91,565 | $14,000 |
| Swarthmore | $23,149 | $7,690 | 92% | $80,257 | $17,500 |
| Northwestern University | $29,167 | $1,764 | 95% | $89,363 | $15,000 |
| Rice University | $13,370 | $5,827 | 95% | $89,718 | $11,000 |
| Cornell University | $28,690 | $1,776 | 95% | $104,043 | $14,000 |
| University of California, Los Angeles | $12,548 | $5,579 | 93% | $82,511 | $14,000 |
| New York University | $37,050 | $16,977 | 88% | $82,509 | $20,500 |
| University of Southern California | $32,740 | $13,516 | 92% | $92,498 | $18,000 |
| University of California, Berkeley | $13,481 | $5,311 | 93% | $92,446 | $13,000 |
| University of Notre Dame | $26,780 | $7,244 | 95% | $99,980 | $19,000 |
| Emory University | $22,585 | $7,363 | 91% | $80,137 | $18,250 |
| Boston University | $24,402 | $9,500 | 89% | $83,238 | $23,250 |
| Tufts University | $39,998 | $11,284 | 94% | $83,214 | $16,250 |
| Carnegie Mellon University | $31,944 | $9,097 | 94% | $114,862 | $21,750 |
| Washington University in St. Louis | $21,786 | $1,716 | 94% | $86,182 | $17,500 |
| Harvey Mudd College | $35,924 | $27,979 | 92% | $138,687 | $25,000 |
| Georgetown University | $40,815 | $5,064 | 95% | $103,494 | $15,500 |
| Georgia Institute of Technology | $12,116 | $7,666 | 94% | $102,772 | $21,672 |
| University of North Carolina at Chapel Hill | $11,655 | $2,004 | 91% | $72,200 | $14,000 |
| University of Michigan | $13,138 | $1,043 | 93% | $83,648 | $19,500 |
| University of Virginia | $21,565 | $8,174 | 96% | $86,863 | $17,500 |
| Wake Forest | $28,719 | $6,525 | 89% | $78,158 | $21,500 |
| University of Florida | $6,541 | $1,982 | 91% | $71,588 | $15,000 |
| Olin College | $25,171 | — | 96% | $129,455 | $19,500 |
| University of Texas at Austin | $19,857 | $12,553 | 89% | $75,121 | $20,500 |
| University of California, San Diego | $12,470 | $7,525 | 86% | $84,943 | $15,500 |
| University of California, Irvine | $14,251 | $8,123 | 87% | $80,735 | $15,000 |
| University of California, Santa Barbara | $16,109 | $9,231 | 83% | $74,915 | $13,993 |
| Case Western Reserve University | $41,190 | $19,025 | 87% | $87,989 | $24,000 |
| University of Washington | $14,091 | $6,384 | 85% | $78,466 | $14,615 |
| University of Rochester | $29,278 | $9,678 | 85% | $79,042 | $21,000 |
| University of Illinois Urbana-Champaign | $14,355 | $2,038 | 85% | $81,054 | $19,500 |
| University of California, Davis | $14,741 | $9,211 | 86% | $80,838 | $13,000 |
| University of Wisconsin-Madison | $17,354 | $4,200 | 90% | $73,792 | $20,484 |
| University of Maryland, College Park | $15,678 | $2,962 | 89% | $82,860 | $19,000 |
| Purdue University | $14,600 | $5,098 | 83% | $72,424 | $19,500 |
| Virginia Tech | $24,953 | $11,689 | 86% | $81,698 | $21,500 |
| Texas A&M University | $21,315 | $12,784 | 84% | $72,097 | $17,804 |
| Rutgers University | $24,406 | $16,343 | 84% | $74,479 | $21,500 |
| Worcester Polytechnic Institute | $43,071 | $24,018 | 90% | $103,470 | $27,000 |
| Ohio State University | $17,339 | $4,885 | 88% | $60,409 | $19,976 |
| Penn State | $32,875 | $19,845 | 86% | $63,435 | $25,000 |
| Rensselaer Polytechnic Institute | $36,228 | $24,078 | 84% | $102,051 | $23,750 |
| University at Buffalo | $20,995 | $14,668 | 75% | $70,814 | $19,000 |
| Rose-Hulman | $42,513 | $36,843 | 78% | $101,253 | $25,000 |
| University of Minnesota | $16,778 | $6,642 | 85% | $69,020 | $19,500 |

## 4. UC and CS/engineering program-level admit rates

### 4a. UC, by campus and broad discipline — PRIMARY SOURCE, now upgraded

**Source:** [UC Information Center, "Freshman admission by discipline"](https://www.universityofcalifornia.edu/about-uc/information-center/freshman-admission-discipline), the UC Office of the President's own public Tableau workbook. No bulk CSV export exists for the by-discipline breakdown (only the campus-overall sheet exports), so these figures were read directly off the live dashboard, campus by campus, for Fall 2023/2024/2025, and hand-transcribed. Full data, all 9 campuses × 3 years × 2 disciplines, plus the definitions: `school_data/uc_by_discipline.json`. This replaces the earlier secondary-sourced version of this section — and confirms it was directionally right (Berkeley CS ~6%, UCSB CS's jump from 17% to 34% both check out exactly against the primary data).

**Important definitional note:** UC's "Computer Science" and "Engineering" are its own *broad-discipline* groupings, not individual majors — "Computer Science" is a distinct bucket from "Engineering" (which includes ECE, ME, and, in UCOP's own grouping, Berkeley's College of Chemistry). This is coarser than "Berkeley EECS vs. L&S CS" — UC's public dashboard doesn't split that finely. GPA ranges below are UC's own recalculated/capped GPA, not a raw high school GPA.

**Computer Science — admit rate, applicants→admits, by campus and year:**

| Campus | 2023 admit% (n) | 2024 admit% (n) | 2025 admit% (n) | 2025 admit GPA (25th–75th) |
|:--|--:|--:|--:|:--|
| Berkeley | 4% (9,018) | 4% (13,437) | 6% (9,750) | 4.20–4.29 |
| UCLA | 3% (11,938) | 4% (10,530) | 7% (6,803) | 4.25–4.30 |
| San Diego | 12% (13,729) | 13% (12,519) | 20% (10,785) | 4.16–4.30 |
| Irvine | 17% (10,071) | 20% (9,187) | 28% (6,794) | 4.17–4.29 |
| Davis | 19% (5,256) | 17% (6,950) | 19% (4,893) | 4.20–4.30 |
| Santa Barbara | 10% (9,821) | 17% (8,560) | 34% (5,865) | 4.19–4.29 |
| Riverside | 49% (5,558) | 54% (5,001) | 81% (5,068) | 3.96–4.25 |
| Santa Cruz | 59% (6,596) | 65% (6,597) | 79% (5,952) | 3.92–4.25 |
| Merced | *(not broken out — too few CS applicants for UC's own reporting threshold)* | | | |

**Engineering — same layout:**

| Campus | 2023 admit% (n) | 2024 admit% (n) | 2025 admit% (n) | 2025 admit GPA (25th–75th) |
|:--|--:|--:|--:|:--|
| Berkeley | 7% (26,470) | 8% (21,831) | 7% (25,025) | 4.20–4.30 |
| UCLA | 6% (20,989) | 6% (22,301) | 7% (23,911) | 4.25–4.32 |
| San Diego | 18% (16,709) | 17% (18,443) | 19% (20,205) | 4.17–4.30 |
| Irvine | 28% (17,832) | 28% (19,342) | 27% (20,276) | 4.15–4.29 |
| Santa Barbara | 18% (10,685) | 21% (11,873) | 21% (12,679) | 4.21–4.30 |
| Davis | 34% (17,505) | 38% (16,933) | 39% (17,866) | 4.08–4.28 |
| Riverside | 61% (7,776) | 70% (8,486) | 84% (11,480) | 3.84–4.22 |
| Santa Cruz | 66% (4,426) | 69% (5,018) | 77% (5,134) | 3.85–4.22 |
| Merced | 90% (6,481) | 93% (6,429) | 97% (11,565) | 3.69–4.21 |

**What this shows that the campus-wide numbers in §1 hide:** at Berkeley and UCLA specifically, CS is roughly **half to a third as likely to admit** as the campus-wide rate suggests (Berkeley campus 11% vs. CS 6%; UCLA campus 9% vs. CS 7% — closer than Berkeley's gap, but still worse). At Riverside, Santa Cruz, and Merced, the opposite: CS/Engineering admit rates are so high (49–97%) that the "broad discipline" grouping is barely gatekeeping at all — these campuses function as a real, high-probability CS/engineering path for a student whose profile doesn't clear Berkeley or UCLA's CS bar. **The Berkeley/UCLA CS trend is also moving in the applicant's favor** — both admit rates roughly doubled from 2023/2024 to 2025 — worth watching for whether that continues rather than assuming today's number holds three years out.

### 4b. Non-UC CS/engineering programs

| Program | Figure | Confidence / source |
|:--|:--|:--|
| **University of Washington, Allen School, direct-to-major CS/CE** | **WA resident: 26% (2023) → 27% (2024) → 37% (2025) → 41% (2026). Domestic non-resident: 2% → 1% → 5% → 8%. International: 2% → 2% → 2% → 4%.** | **PRIMARY SOURCE** — [UW Allen School's own published admissions statistics page](https://www.cs.washington.edu/academics/undergraduate/admissions/direct-major), by year and residency status. The non-resident/international rates are startlingly low and have been recovering the last two cycles; WA-resident applicants have a categorically better shot. |
| CMU School of Computer Science | **Cross-checked: "under 5%" is directionally right but stale, and the only better number found is also old.** CMU's own SCS department page states that for the **2015** cycle, "Only 350 were admitted — a rate of less than 5.2 percent" out of 6,756 applicants ([cs.cmu.edu/link/meeting-demand](https://www.cs.cmu.edu/link/meeting-demand), primary, CMU's own words). That's a real CMU-stated figure, but it's a decade old and every other source found (multiple consultancy sites) just repeats "under 5%" with no independent number — none diverge, but none are current either. Combined with the Fall-2012 Wayback-recovered factbook data already in this row (SCS had the highest mean SAT of any CMU college that year), the picture is consistent but nothing here is from the current decade. | PRIMARY for both numbers (2015 CS statement, 2012 factbook) — **not current**. No 2020s-era CMU-stated figure was found anywhere. |
| UC Berkeley EECS (College of Engineering, direct admit, distinct from the L&S "Computer Science" broad-discipline figures in §4a) | **Cross-checked and corrected — "under 5%" was wrong.** Two independent sources converge on **7.6% for Fall 2024** (421 admitted of 5,482 applicants, "before any waitlist activity"), attributed to a Berkeley Counselor Bulletin (April 2024) — a communication Berkeley sends to high school counselors — and separately repeated in a College Confidential thread citing the same figure. The same bulletin states Berkeley's overall first-year admit rate was 11.4% that cycle, so EECS ran about two-thirds as selective as the campus average — a real gap, but nowhere near the "<5%" previously listed here. | Secondary (a counselor-bulletin figure relayed by two independent sites, not an official Berkeley webpage directly verified) — but **specific, recent (Fall 2024), and mutually corroborating**, so meaningfully stronger than the single unsourced "<5%" consultancy claim it replaces. [askmssun.com writeup](https://askmssun.com/berkeley-first-year-admit-rates-most-popular-majors-fall-2024/); corroborated at [College Confidential](https://talk.collegeconfidential.com/t/ucb-eecs-and-ba-cs-acceptance-rates/3668376). |
| UIUC, Computer Science (Siebel School) | **Partially confirmed by the university itself, though not with an exact year-tagged figure.** UIUC's own admissions site ([admissions.illinois.edu/apply/freshman/admit-rate](https://www.admissions.illinois.edu/apply/freshman/admit-rate)) publishes real, current, college-level "first-choice major" admit rates for Fall 2026: Grainger College of Engineering (CS's parent college) **23.3%**, Gies Business 22.5%, LAS 40.6%, overall 38.1% — but does **not** break out CS specifically at the college-level table checked. However, the **Siebel School of Computing and Data Science's own FAQ page** ([siebelschool.illinois.edu](https://siebelschool.illinois.edu/academics/undergraduate/degree-program-options/cs-undergraduate-degree-options-faq), the CS department itself, not a consultancy) directly states CS "has an admit rate of less than 7%" and that CS "has broken the record for the most first-year applications received by any program in the university's history" — no exact percentage or year given, but this is now department-confirmed rather than blog-sourced. The commonly cited "~7.4%" figure is consistent with this but its exact year/source is still unverified. | PARTIALLY PRIMARY — Grainger-level rate is primary and current (Fall 2026); the CS-specific "<7%" is primary-sourced to the CS department's FAQ but without a precise figure or year. |
| **Georgia Tech, College of Computing** | **Upgraded to PRIMARY SOURCE, and current.** Georgia Tech's own IRP Fact Book publishes "Freshman Admissions by Year and College" every year: College of Computing went Fall 2019 14.5% (8,190 applicants → 1,190 admits) → Fall 2020 16.5% → Fall 2021 13.5% → Fall 2022 12.8% → **Fall 2023 10.4%** (14,732 → 1,533) — a clear multi-year decline as applications nearly doubled. Same table, Fall 2023: College of Engineering 15.6% (22,952 applicants), College of Sciences 21.2%, Ivan Allen (liberal arts) 21.5%, Scheller (business) 16.5%; Institute-wide 15.3%. This replaces the earlier "~4–6% out-of-state" estimate — the old "12.8% for Class of 2030" figure turns out to match Fall 2022 exactly, so it was likely a mislabeled year rather than a wrong number. Georgia Tech doesn't publish a narrower split within Computing (no separate CS vs. other Computing majors), so College of Computing is the finest grain available here. | **PRIMARY SOURCE** — [Georgia Tech IRP 2023 Fact Book](https://irp.gatech.edu/sites/default/files/FactBook/FactBook_2023.pdf), p.1, "Freshman Admissions by Year and College, Fall Terms." Current through Fall 2023 (most recent fact book published). |
| Purdue, Computer Science | **Cross-checked and corrected — Purdue now publishes this.** Purdue's own admissions site currently lists an "Enrollment by Competitive Majors" table giving **Computer Science: 42.9% admit rate** (Fall 2025), SAT middle-50% 1420–1530, ACT middle-50% 33–35 — notably *more* selective than its own parent College of Science (46.0%) but far above the sub-5% range some CS programs run at. This appears to be a recent change from what Purdue's CS department told earlier inquirers (that per-major rates weren't published); the department-level statement may simply be outdated now, or the university-level page may have started publishing what individual departments don't. | **PRIMARY SOURCE** — [admissions.purdue.edu/academics/freshmanprofile.php](https://admissions.purdue.edu/academics/freshmanprofile.php), current (Fall 2025 cycle), verified directly. |
| Cornell, College of Engineering | **Chased down — real data found, but too stale to use as current.** Cornell's factbook archive's only by-college applicant/admit breakdown is frozen at **Fall 2011**: Engineering that year was 8,696 applicants → 1,787 admits (20.5%), actually *less* selective than Arts & Sciences (17,057 → 2,641, 15.5%) and than the university overall (18.0%) — the opposite of the "CS/Engineering is hardest" pattern seen at UC and UW above. Cornell's university-wide admit rate has since roughly halved (18.0% in 2011 → 8.7% for the Class of 2025/Fall 2021 cohort → 9% per the current CDS in §1), so this 2011 relative-selectivity pattern should **not** be assumed to still hold — it's a historical data point, not a current one. | PRIMARY SOURCE for what it covers ([Engineering 1990-2011 PDF](http://irp.cornell.edu/wp-content/uploads/2024/04/1000147.pdf), [By College Fall 2011 PDF](http://irp.cornell.edu/wp-content/uploads/2024/04/1000003.pdf)) — but 14+ years out of date. No more recent by-college breakdown was found on Cornell's IRP site. |
| Cornell, ED vs. RD admit rate (university-wide, not by college) | **New primary-sourced data point:** Class of 2025 (Fall 2021 entering) — ED 9,017 applicants → 1,930 admits (**21.4%**); RD 58,363 → 3,922 (**6.7%**). A genuinely large gap, and a real, if dated, number to use in place of the "—" in §1's ED admit % column, which this pass could not otherwise fill for Cornell. | PRIMARY SOURCE — [Cornell Class of 2025 first-year profile PDF](http://irp.cornell.edu/wp-content/uploads/2021/10/Profile2021-first-year.pdf), Cornell IRP. Also shows Engineering was 897 of 3,765 enrolling first-years that year (23.8% of the class) — enrollment share, not an admit rate, since this document doesn't break applicants/admits down by college. |

**Practical reading for a CS-focused applicant:** everywhere this has been checked against a primary source (UC's own dashboard, UW's own page), the *program* is meaningfully harder to enter than the campus-wide rate implies, and the gap is largest at the most selective campuses (Berkeley, UCLA, UW non-resident) and smallest or inverted at less selective ones (Riverside, Merced, Santa Cruz, UW in-state). Where a school admits by major, don't use the campus-wide number in §1 as a proxy for CS odds specifically.

**To go further:** CMU's current (post-2015) per-college admit table and an exact, year-tagged UIUC CS admit rate remain the open gaps — everything else in this table is now either primary-current (Georgia Tech, Purdue, UW) or a specific, corroborated, recent secondary figure (Berkeley EECS).

**Cross-check pass results (2026-09-22):** this row-by-row cross-check against independent sources caught one real error (Berkeley EECS was listed as "<5%"; the actual current figure is ~7.6%) and one stale assumption (Purdue was listed as "not published"; it now is, at 42.9%). Both are corrected above. This is the value of cross-checking even "settled" secondary claims — the Berkeley number in particular had been repeated across multiple consultancy sites without anyone tracing it to an actual data point.

### 4c. Admission structure: direct-admit vs. unified-then-declare vs. competitive-declare

**Why this matters more than the exact rate:** two schools with the same headline admit rate can be entirely different bets for a CS-focused applicant. At a "direct-admit" school, the admissions decision on CS is essentially final at the point of application — get in as undeclared or a different major, and CS may be closed to you later. At a "unified" school, the campus-wide admit rate *is* your real odds of eventually doing CS, since declaring it later is close to automatic. In between are "competitive-declare" schools, where admission to the university tells you little — the real gate is a GPA/prerequisite hurdle cleared (or not) after enrolling, often invisible to an applicant just reading the admit-rate headline. Verified against each school's own admissions or CS-department page (not secondary blogs); each row below is sourced individually.

**Direct-admit** (CS or Engineering admission decided at application; switching in later is difficult, capped, or closed):

| School | Mechanism | Source |
|:--|:--|:--|
| Carnegie Mellon University | Applicants apply directly to a specific college (e.g. School of Computer Science); internal transfer in requires ~3.6 QPA in core CS courses and is not guaranteed. | [cmu.edu/admission](https://www.cmu.edu/admission/admission/admission-consideration) |
| University of Pennsylvania | CS as a primary/sole major requires admission to SEAS; College (Arts & Sciences) students can only add CS as a secondary major, and inter-school transfer is difficult. | [cis.upenn.edu](https://www.cis.upenn.edu/undergraduate/undergraduate-program-options/) |
| UCLA | CS selected on the UC application; change-of-major into CS later requires a 3.7 prep GPA and near-impossible odds. | [seasoasa.ucla.edu](https://www.seasoasa.ucla.edu/change-of-major-2/) |
| UC San Diego | CS selected on the application; non-admitted students face a capped, once-yearly "Selective Major" process with no guarantee. | [cse.ucsd.edu](https://cse.ucsd.edu/undergraduate/cse-selective-major-process) |
| UC Irvine | CS selected on the application; switching in later needs a 2.7–3.0 GPA threshold and departmental capacity limits. | [changeofmajor.uci.edu](https://changeofmajor.uci.edu/school-of-information-and-computer-sciences) |
| UC Davis | CS selected on the application (College of Engineering as of Fall 2024); switching in later needs a 3.0 GPA prep sequence and a capacity cap. | [cs.ucdavis.edu](https://cs.ucdavis.edu/undergraduate/changing-majors-double-majors) |
| UC Santa Barbara | Applied to directly within the College of Engineering; post-enrollment change-of-major into CS is "extremely rare" and barred for transfer students entirely. | [admissions.sa.ucsb.edu](https://admissions.sa.ucsb.edu/major-changes) |
| Georgia Institute of Technology | Since Summer 2024, students admitted without CS as first-choice major "will not have the option" to change into it; reopened only on limited, space-available basis. | [cc.gatech.edu](https://www.cc.gatech.edu/create-application-changing-majors-computer-science) |
| University of Texas at Austin | CS admitted directly within the College of Natural Sciences; internal transfer requires 3.0 GPA, space-available admission, capped at two attempts. | [cns.utexas.edu](https://cns.utexas.edu/info-undergraduate-students/academics-advising-policies/internal-transfer) |
| University of Illinois Urbana-Champaign | CS (and CS+Bioengineering, CS+Physics) is "closed to all on-campus transfer" — no petition or major-change route once enrolled outside Grainger. | [grainger.illinois.edu](https://grainger.illinois.edu/academics/undergraduate/changing-majors) |
| Purdue University | CS selected at application as a "space restricted program"; the CODO (change-of-degree-objective) switch-in process runs once per term, decisions final, no appeal. | [cs.purdue.edu](https://www.cs.purdue.edu/undergraduate/codo.html) |
| University of Maryland, College Park | CS is a Limited Enrollment Program with direct freshman admission plus a 45-credit performance review; internal transfer for others is "extremely limited." | [undergrad.cs.umd.edu](https://undergrad.cs.umd.edu/internal-transfer-applicants) |
| University of Southern California | CS (Viterbi/VSE) listed as first-choice major at application; entry from outside Viterbi later is separate and competitive. | [viterbiadmission.usc.edu](https://viterbiadmission.usc.edu/apply/) |
| Northeastern University | Applicants apply to and are admitted into Khoury College of Computer Sciences as their college; switching in later requires placement exams, prerequisites, and department approval. | [admissions.northeastern.edu](https://admissions.northeastern.edu/colleges/khoury-college-of-computer-sciences/) |
| Washington University in St. Louis | Applicants select one of WashU's undergraduate schools (incl. Engineering, which houses CS) at application; transferring schools later is a separate process. | [admissions.washu.edu](https://admissions.washu.edu/how-to-apply/common-questions/) |
| Rensselaer Polytechnic Institute | Admitted to the specific major indicated on the application; switching later uses a straightforward Change-in-Major form — less restrictive than most peer direct-admit schools. | [undergrad.admissions.rpi.edu](https://undergrad.admissions.rpi.edu/accepted-students/frequently-asked-questions) |
| Vanderbilt University | *In transition as of Sept. 2026*: historically Engineering-housed CS with GPA-gated Intra-University Transfer; a new College of Connected Computing now takes direct first-year CS applicants (opened Aug. 2026). | [computing.vanderbilt.edu](https://computing.vanderbilt.edu/undergraduate-programs/) |

**Hybrid — two separate colleges both lead to a CS degree, each with its own admission pool:**

| School | Mechanism | Source |
|:--|:--|:--|
| Cornell University | CS reachable via College of Engineering (BS) or College of Arts & Sciences (BA), each a separately admitting college. | [bowers.cornell.edu](https://bowers.cornell.edu/undergraduate-opportunities/computer-science) |
| Columbia University | CS offered as a B.A. via Columbia College and a B.S. via Columbia Engineering (SEAS) — separate applicant pools; "the CS department does not process undergraduate admissions." | [cs.columbia.edu](https://www.cs.columbia.edu/education/undergraduate/prospectivefaq/) |
| Northwestern University | Joint CS department offering a BS via McCormick Engineering or a BA via Weinberg College of Arts & Sciences; applicants pick one of Northwestern's six schools at application. | [mccormick.northwestern.edu](https://www.mccormick.northwestern.edu/computer-science/academics/undergraduate/cs-major/) |
| New York University | CS reachable via College of Arts & Science (Courant, BA) or Tandon School of Engineering (BS) — chosen directly on the Common App as two separate schools/programs. | [cs.nyu.edu](https://cs.nyu.edu/dynamic/undergraduates/cs-major/cs-at-cas-and-tandon/) |
| University of Michigan | CS reachable via College of Engineering or LSA, each a separate admission track; since Fall 2023 **both** require a competitive "advance selection" step at application due to capacity limits (so also partly "competitive-declare"). | [cse.engin.umich.edu](https://cse.engin.umich.edu/academics/undergraduate/admissions/cs-advance-selection-for-incoming-students/) |
| University of California, Berkeley | Applicants pick either EECS (College of Engineering) or CS (College of Computing, Data Science & Society, CDSS); **both are now direct-admit-by-major as of Fall 2023** — CDSS's own FAQ states admitted CS students are auto-enrolled, "no further steps are needed." This retires Berkeley's old reputation as a hard-to-declare L&S major. | [cdss.berkeley.edu](https://cdss.berkeley.edu/admissions) |
| University of Virginia | BACS (Arts & Sciences) and BSCS (Engineering) are separate degrees admitted through separate schools; declaring CS within either school is open once prerequisites are met — no competitive gate once you're in the right school. | [engineering.virginia.edu](https://engineering.virginia.edu/department/computer-science/academics/cs-undergraduate-programs) |

**Secondary/competitive-declare — broadly admitted, but a real post-enrollment gate stands between you and the CS major:**

| School | Mechanism | Source |
|:--|:--|:--|
| University of Washington | Most first-years now apply via a selective Direct-to-Major process (admit rate 4–41% by residency, per §4b); non-selected "pre-major" students face a separate, historically low-odds internal path. | [cs.washington.edu](https://www.cs.washington.edu/academics/undergraduate/admissions/direct-major) |
| University of Wisconsin-Madison | Admitted broadly to L&S; declaring CS later requires a "BC" grade in intro programming plus a 2.25 GPA threshold — a hard, non-automatic gate. | [cs.wisc.edu](https://www.cs.wisc.edu/faqs-for-prospective-students-extended-version/) |
| University of North Carolina at Chapel Hill | Admitted broadly; declaring CS requires a holistic, capacity-restricted application (essays, coursework review) submitted after completing COMP 210. | [cs.unc.edu](https://cs.unc.edu/undergraduate/cs-admissions/) |
| Virginia Tech | First-year CS applicants start in General Engineering; entering the CS major later requires prerequisites plus a 3.0 GPA for a guaranteed first-choice spot. | [eng.vt.edu](https://eng.vt.edu/undergraduate/orientation/frequently-asked-questions.html) |
| Texas A&M University | Admitted to Engineering with a noted major "preference," not directly into CS; entering CS requires the competitive Entry-to-a-Major (ETAM) process. | [engineering.tamu.edu](https://engineering.tamu.edu/cse/admissions-and-aid/undergraduate-admissions/index.html) |
| Ohio State University | CS "pre-major" chosen at application (can't switch in from elsewhere later); full major status requires a competitive ~3.2 GPA plus prerequisite coursework. | [cse.osu.edu](https://cse.osu.edu/prospective-students/undergrad/admission-major) |
| Penn State | Enter as pre-major/undeclared; University Park's "entrance to major" for CS requires a 3.20 cumulative GPA plus specific prerequisite courses. | [bulletins.psu.edu](https://bulletins.psu.edu/undergraduate/colleges/engineering/computer-science-bs/) |
| University of Minnesota | Both the CLA (B.A.) and CSE (B.S.) CS tracks share a competitive technical-GPA gate: 3.2 guarantees entry, below that is space-available. | [cse.umn.edu](https://cse.umn.edu/cs/ug-admissions-overview) |
| University of Florida | Freshmen declare CS freely at orientation, but must clear "critical-tracking" courses with C grades and a 2.5 GPA to remain in the major or be dismissed from it. | [catalog.ufl.edu](https://catalog.ufl.edu/UGRD/colleges-schools/UGENG/CPS_BSCS/) |
| Princeton University | Applicants indicate A.B./B.S.E./undecided non-bindingly; switching from A.B./Undecided into B.S.E. (which houses CS) requires a short application reviewed for math/physics preparation. | [advising.princeton.edu](https://advising.princeton.edu/degree-planning/choosing-degree-ab-and-bse) |

**Unified/admit-then-declare — admitted to the university broadly; declaring CS later has no real competitive gate:**

MIT, Stanford, Harvard, Yale, University of Chicago, Dartmouth, Brown, Duke (Trinity College only — CS doesn't exist in Pratt Engineering), Johns Hopkins, Rice, Georgetown (College only — CS doesn't exist in the other three schools), Case Western Reserve, University of Rochester, Emory, Boston University, Worcester Polytechnic Institute, Rutgers–New Brunswick (declare after C-or-better in five prerequisites, not stated as capacity-limited). Individual sourcing for each of these is in the full agent research output; the common pattern is a school-specific "declare your major" page with no GPA/capacity gate mentioned, in contrast to the competitive-declare list above.

**Reading this table with the rest of §4:** a "direct-admit" or "competitive-declare" school's *campus-wide* admit rate (§1) systematically overstates a CS applicant's real odds — the meaningful number is whatever CS-specific rate exists in §4a/§4b, or, absent that, an assumption that CS is harder than the headline. A "unified" school is the one case where §1's campus-wide rate *is* a reasonable proxy for CS odds, since declaring CS later is close to automatic. This is especially relevant for reading the archive (`combined_profiles.json`): a profile that names a school without naming CS specifically, at a direct-admit school, may not represent a CS admit at all.

Joined from `combined_profiles.json` (only profiles with a **confirmed** commitment and a parseable self-reported SAT; schools with ≥8 such profiles). Percentages are shares of those profiles. **Caveats:** self-reported; test-optional applicants who didn't submit are invisible here, which biases the archive toward high scorers; SAT ranges are the approximate section-sum ranges from §1; only ~850 of 1,215 confirmed profiles report a parseable SAT.

| School | n | Below school's 25th pct | Within middle 50% | Above 75th pct |
|:--|--:|--:|--:|--:|
| University of Pennsylvania | 53 | 26% | 57% | 17% |
| Cornell University | 48 | 29% | 65% | 6% |
| Yale University | 37 | 19% | 70% | 11% |
| University of California, Berkeley | 35 | 9% | 37% | 54% |
| Stanford University | 34 | 18% | 76% | 6% |
| Georgia Institute of Technology | 34 | 0% | 47% | 53% |
| Duke University | 34 | 9% | 71% | 21% |
| Brown University | 31 | 26% | 68% | 6% |
| Massachusetts Institute of Technology | 30 | 37% | 37% | 27% |
| Harvard University | 30 | 33% | 60% | 7% |
| Princeton University | 29 | 21% | 69% | 10% |
| New York University | 27 | 30% | 59% | 11% |
| University of California, Los Angeles | 26 | 4% | 54% | 42% |
| University of Southern California | 25 | 28% | 44% | 28% |
| University of Michigan | 24 | 17% | 58% | 25% |
| Carnegie Mellon University | 23 | 17% | 65% | 17% |
| Johns Hopkins University | 23 | 26% | 65% | 9% |
| Columbia University | 22 | 27% | 50% | 23% |
| University of Chicago | 20 | 5% | 80% | 15% |
| Purdue University | 19 | 5% | 42% | 53% |
| University of Illinois Urbana-Champaign | 18 | 0% | 39% | 61% |
| Northwestern University | 16 | 44% | 50% | 6% |
| University of California, San Diego | 13 | 0% | 31% | 69% |
| University of Virginia | 12 | 8% | 75% | 17% |
| Dartmouth College | 11 | 9% | 55% | 36% |
| University of Florida | 10 | 0% | 50% | 50% |
| Northeastern University | 10 | 30% | 50% | 20% |
| University of Texas at Austin | 10 | 10% | 20% | 70% |
| Emory University | 10 | 40% | 30% | 30% |
| Vanderbilt University | 9 | 33% | 67% | 0% |
| Rice University | 8 | 12% | 88% | 0% |
| University of Washington | 8 | 0% | 25% | 75% |
| University of Notre Dame | 8 | 25% | 50% | 25% |
| Boston University | 8 | 50% | 38% | 12% |
| Washington University in St. Louis | 8 | 38% | 50% | 12% |
| Case Western Reserve University | 8 | 25% | 62% | 12% |
| University of North Carolina at Chapel Hill | 8 | 0% | 62% | 38% |

The 'below 25th percentile' column is informative in itself: at most schools a non-trivial minority of confirmed enrollees in this archive scored under the school's published 25th percentile, consistent with the practitioner advice (AMA file) that scores are a threshold check, not a ranking.
**Read with care:** UC campuses are test-blind, so their SAT ranges (and the high "above 75th" share at Berkeley) reflect only the few students whose scores were ever reported, not what the campus uses. Section-sum ranges are wider than true composite ranges, so "below 25th" is, if anything, understated. Small-n rows (n under ~30) are noisy.

## 6. Ten-year admit-rate trend, 2014 → 2024 (federal IPEDS)

**Source:** federal IPEDS data (`ipeds_facts`, via the same collegedata.fyi API used for §1–3), pulled per school for every year 2014–2024 rather than just the latest year. Machine-readable: `school_data/school_admit_trends.json` (full year-by-year series) and `school_data/ipeds_trends_raw.json` (raw pull, all available fields including SAT/ACT/yield/retention/grad-rate, back to 2004 where reported). This section replaces the earlier single-year-snapshot limitation of §1: every number below is now a decade of context, not one data point.

**Headline pattern:** every one of the 60 schools saw applicant volume roughly double (or more) from 2014 to 2024 — the Common App/Coalition App era made applying to more schools nearly costless — but the *admit rate* response split into two clearly different groups.

**Sorted by admit-rate change, most-declined first (selected rows; full 60-school table in the JSON):**

| School | 2014 admit % | 2024 admit % | Change | Applicant volume change |
|:--|--:|--:|--:|--:|
| Northeastern University | 32% | 5% | −27pt | +98% |
| New York University | 35% | 9% | −26pt | +118% |
| Boston University | 35% | 11% | −24pt | +45% |
| University of Florida | 46% | 24% | −22pt | +157% |
| Georgia Institute of Technology | 33% | 14% | −19pt | +131% |
| University of Illinois Urbana-Champaign | 59% | 42% | −17pt | +106% |
| University of Michigan | 32% | 16% | −16pt | +98% |
| University of Washington | 55% | 39% | −16pt | +119% |
| Carnegie Mellon University | 25% | 12% | −13pt | +71% |
| University of North Carolina at Chapel Hill | 28% | 15% | −13pt | +112% |
| Johns Hopkins University | 16% | 6% | −10pt | +87% |
| University of California, Los Angeles | 19% | 9% | −10pt | +69% |
| Massachusetts Institute of Technology | 8% | 5% | −3pt | +54% |
| Harvard University | 6% | 4% | −2pt | +58% |
| Stanford University | 5% | 4% | −1pt | +36% |
| University of California, Davis | 40% | 42% | +2pt | +63% |
| Penn State | 50% | 61% | +11pt | +76% |
| Worcester Polytechnic Institute | 44% | 60% | +16pt | +23% |
| University at Buffalo | 58% | 74% | +16pt | +67% |
| Rose-Hulman | 59% | 77% | +18pt | +38% |
| Rensselaer Polytechnic Institute | 38% | 63% | +25pt | −8% |
| University of Minnesota | 45% | 80% | +35pt | −7% |

**How to read this:**
- **The already-elite schools (Harvard, Stanford, MIT, Princeton, Yale, Columbia) moved the *least* in percentage points** — they were already near a floor, so the story there is less "getting harder" and more "already impossibly hard, staying impossibly hard" while absorbing 50–85% more applications on a fixed class size.
- **The biggest percentage-point drops are concentrated in large publics and upper-tier privates that were previously "high-match" schools** (Northeastern, NYU, BU, UF, Georgia Tech, UIUC, Michigan, UW) — these are the schools where "it got dramatically harder in the last decade" is a *true, quantified* statement, not perception. Northeastern in particular went from a safety/match school to a reach in ten years — a genuinely useful, specific fact for the archive and reference docs, since older forum profiles calling Northeastern a "safety" reflect a real, dated reality, not sloppy self-assessment.
- **A distinct cluster of schools *increased* their admit rate** — Minnesota, RPI, Rose-Hulman, Buffalo, WPI, Penn State, Ohio State, UC Davis, Rochester, Olin. Several of these (RPI, Minnesota) show *falling* applicant volume alongside a rising admit rate, suggesting a genuine demand softening rather than just enrollment-growth strategy; others (Buffalo, WPI, Rose-Hulman) grew applications modestly while admitting a larger share, consistent with deliberate class-size expansion. Worth treating these as a "less selectivity-inflated" list for a student whose profile doesn't clear the reach-school bar above.
- **This directly refines §1's static admit-rate column**, which is a single (current) year and gives no sense of trajectory. A school at, say, 15% today that was 28% a decade ago (UNC) is a fundamentally different admissions environment than a school that has held steady at 15% throughout.

**Caveats:** IPEDS `admit_rate_total` is a whole-institution figure (matches §1's methodology, not §4's program-level data). Years before 2014 exist in the raw JSON for some fields but admit-rate coverage is sparse/unreliable before 2014, so the comparison window was fixed at 2014→2024 for consistency across all 60 schools. "Applicant volume change" is a blunt instrument — it doesn't distinguish genuinely more-interested applicants from Common App drive-by applications, which is itself part of why raw admit rate has become a noisier signal over the same period.
