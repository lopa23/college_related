# School Admissions Data Reference (CDS + IPEDS)

> **What this is:** Official-source numbers (Common Data Set filings + federal IPEDS/NCES data) for 60 schools relevant to elite and CS/engineering admissions, to give the profile archive and the book/AMA files a real denominator. Machine-readable versions: `school_data/school_facts.json` (§1–3) and `school_data/uc_by_discipline.json` (§4a, UC by campus/discipline/year).
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
| CMU School of Computer Science | **"under 5%" (CMU overall ~11%) is still unconfirmed as a current admit rate** — no per-college applicant/admit table exists on CMU's live IRA site. **But real, if dated, primary data was recovered:** CMU's Factbook series (its official by-college statistical publication) was discontinued after 2012-13, and even the archive page listing it (`factbook-archive/facts2013.html`) links to PDFs that are now dead on CMU's live site. The Fall-2012 edition was recovered via the Wayback Machine (archived Apr 2025, since the live copy was still up then). It confirms — as of Fall 2012 — SCS (Computer Science) had the highest mean SAT of any CMU college (1526, vs. 1422 for CIT/Engineering and 1406 university-wide), and CMU's overall admit rate was already falling fast (37.9% in 2008 → 27.8% in 2012). It does **not** give per-college applicant/admit counts, only enrollment headcounts and SAT means by college, so a per-college *admit rate* still can't be computed even from this primary source — but the SCS > CIT > university-average selectivity ordering is now primary-sourced, even though the exact "<5%" figure for today isn't. | PRIMARY SOURCE for what it covers, recovered via Wayback Machine from CMU's own now-broken link ([Fall 2012 Admission & First-Year Enrollment PDF](http://web.archive.org/web/20250410190125/https://www.cmu.edu/ira/factbook/pdf/facts2013/admission-and-first-year-enrollment-pdf-for-web.pdf)) — 14 years stale as of today. |
| UC Berkeley EECS (College of Engineering, direct admit, distinct from the L&S "Computer Science" broad-discipline figures in §4a) | "under 5%" | Consultancy estimate (Oriel Admissions) — not confirmed against a primary EECS-specific source; §4a's Berkeley "Computer Science" row is the closest primary-sourced figure but is not EECS-specific |
| UIUC, Computer Science (Siebel School) | **Partially confirmed by the university itself, though not with an exact year-tagged figure.** UIUC's own admissions site ([admissions.illinois.edu/apply/freshman/admit-rate](https://www.admissions.illinois.edu/apply/freshman/admit-rate)) publishes real, current, college-level "first-choice major" admit rates for Fall 2026: Grainger College of Engineering (CS's parent college) **23.3%**, Gies Business 22.5%, LAS 40.6%, overall 38.1% — but does **not** break out CS specifically at the college-level table checked. However, the **Siebel School of Computing and Data Science's own FAQ page** ([siebelschool.illinois.edu](https://siebelschool.illinois.edu/academics/undergraduate/degree-program-options/cs-undergraduate-degree-options-faq), the CS department itself, not a consultancy) directly states CS "has an admit rate of less than 7%" and that CS "has broken the record for the most first-year applications received by any program in the university's history" — no exact percentage or year given, but this is now department-confirmed rather than blog-sourced. The commonly cited "~7.4%" figure is consistent with this but its exact year/source is still unverified. | PARTIALLY PRIMARY — Grainger-level rate is primary and current (Fall 2026); the CS-specific "<7%" is primary-sourced to the CS department's FAQ but without a precise figure or year. |
| **Georgia Tech, College of Computing** | **Upgraded to PRIMARY SOURCE, and current.** Georgia Tech's own IRP Fact Book publishes "Freshman Admissions by Year and College" every year: College of Computing went Fall 2019 14.5% (8,190 applicants → 1,190 admits) → Fall 2020 16.5% → Fall 2021 13.5% → Fall 2022 12.8% → **Fall 2023 10.4%** (14,732 → 1,533) — a clear multi-year decline as applications nearly doubled. Same table, Fall 2023: College of Engineering 15.6% (22,952 applicants), College of Sciences 21.2%, Ivan Allen (liberal arts) 21.5%, Scheller (business) 16.5%; Institute-wide 15.3%. This replaces the earlier "~4–6% out-of-state" estimate — the old "12.8% for Class of 2030" figure turns out to match Fall 2022 exactly, so it was likely a mislabeled year rather than a wrong number. Georgia Tech doesn't publish a narrower split within Computing (no separate CS vs. other Computing majors), so College of Computing is the finest grain available here. | **PRIMARY SOURCE** — [Georgia Tech IRP 2023 Fact Book](https://irp.gatech.edu/sites/default/files/FactBook/FactBook_2023.pdf), p.1, "Freshman Admissions by Year and College, Fall Terms." Current through Fall 2023 (most recent fact book published). |
| Purdue, Computer Science | not published; Purdue overall ~43% | Purdue's CS department states freshman CS admit rates are not published separately — treat any per-major Purdue figure you see online skeptically |
| Cornell, College of Engineering | **Chased down — real data found, but too stale to use as current.** Cornell's factbook archive's only by-college applicant/admit breakdown is frozen at **Fall 2011**: Engineering that year was 8,696 applicants → 1,787 admits (20.5%), actually *less* selective than Arts & Sciences (17,057 → 2,641, 15.5%) and than the university overall (18.0%) — the opposite of the "CS/Engineering is hardest" pattern seen at UC and UW above. Cornell's university-wide admit rate has since roughly halved (18.0% in 2011 → 8.7% for the Class of 2025/Fall 2021 cohort → 9% per the current CDS in §1), so this 2011 relative-selectivity pattern should **not** be assumed to still hold — it's a historical data point, not a current one. | PRIMARY SOURCE for what it covers ([Engineering 1990-2011 PDF](http://irp.cornell.edu/wp-content/uploads/2024/04/1000147.pdf), [By College Fall 2011 PDF](http://irp.cornell.edu/wp-content/uploads/2024/04/1000003.pdf)) — but 14+ years out of date. No more recent by-college breakdown was found on Cornell's IRP site. |
| Cornell, ED vs. RD admit rate (university-wide, not by college) | **New primary-sourced data point:** Class of 2025 (Fall 2021 entering) — ED 9,017 applicants → 1,930 admits (**21.4%**); RD 58,363 → 3,922 (**6.7%**). A genuinely large gap, and a real, if dated, number to use in place of the "—" in §1's ED admit % column, which this pass could not otherwise fill for Cornell. | PRIMARY SOURCE — [Cornell Class of 2025 first-year profile PDF](http://irp.cornell.edu/wp-content/uploads/2021/10/Profile2021-first-year.pdf), Cornell IRP. Also shows Engineering was 897 of 3,765 enrolling first-years that year (23.8% of the class) — enrollment share, not an admit rate, since this document doesn't break applicants/admits down by college. |

**Practical reading for a CS-focused applicant:** everywhere this has been checked against a primary source (UC's own dashboard, UW's own page), the *program* is meaningfully harder to enter than the campus-wide rate implies, and the gap is largest at the most selective campuses (Berkeley, UCLA, UW non-resident) and smallest or inverted at less selective ones (Riverside, Merced, Santa Cruz, UW in-state). Where a school admits by major, don't use the campus-wide number in §1 as a proxy for CS odds specifically.

**To go further:** CMU's current (post-2013) per-college admit table and an exact, year-tagged UIUC CS admit rate remain the open gaps. Georgia Tech is now fully resolved (primary, current). Purdue's CS department has stated it doesn't publish this figure at all, so that one is likely a permanent gap rather than a research failure.

## 5. Archive cross-check: where confirmed enrollees' SAT scores fall vs. their school's range

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
