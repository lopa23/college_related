# M_college_related — project structure

A knowledge base for elite/CS college admissions research, combining a large Reddit/College Confidential profile archive with institutional data, lawsuit disclosures, and practitioner-voice content (admissions office blogs/podcasts/webinars, book references, AMA testimony).

Reorganized 2026-09-23 into four category folders, split by content type:

```
M_college_related/
├── College Advising Knowledge Base & Triage Engine.md   # core triage framework, kept at root
│
├── qualitative_insights/        # blogs, podcasts, AMAs, webinars, book guides — practitioner-voice content
│   ├── Admissions Book Reference & Profile Query Guide.md
│   ├── Admissions Office Blogs & Podcasts Insights.md
│   ├── Admissions Office Webinars & Virtual Info Session Insights.md
│   ├── Admissions Officer AMA Insights & Profile Query Guide.md
│   ├── Independent Admissions Consultancy Webinars.md
│   ├── MIT Admissions Blog Insights & Process Guide.md
│   ├── More University Admissions Blogs (UChicago, Vanderbilt, Case Western, Rochester).md
│   └── books/
│
├── institutional_data/          # macro admissions stats, yield, legal datasets — hard numbers
│   ├── College Scorecard Field-of-Study Earnings (CS & Engineering).md
│   ├── Common App Aggregate Data Trends.md
│   ├── NACAC State of College Admission Data.md
│   ├── Parchment Cross-Admit Yield Data.md
│   ├── School Admissions Data Reference (CDS + IPEDS).md
│   ├── SFFA Lawsuit Data (Harvard & UNC).md
│   ├── State Percent Plans & Guaranteed Admission Policies.md
│   └── school_data/            # raw pulls + build scripts backing the .md files above (CDS/IPEDS JSON, national IPEDS CSVs, Scorecard field-of-study CSVs, UC Tableau data)
│
├── applicant_profiles/          # the Reddit/College Confidential profile archive
│   ├── combined_profiles.json  # ~2,402 profiles, the central data asset of the whole project
│   ├── processeddata.csv
│   ├── reditt_results.md
│   └── applicant_profile_to_query/
│
└── pipeline/                    # scraper scripts and checkpoint/progress state
    ├── redditt_scrapper.py
    ├── rows_index.json
    ├── enrichment_progress.json
    ├── cc_enrichment_progress.json
    └── chanceme_enrichment_progress.json
```

**How the pieces relate:** `applicant_profiles/combined_profiles.json` is the central dataset — real profile narratives, joined against `institutional_data/school_data/school_facts.json` for a subset with confirmed commitments (see `school_data/join_profiles.py`). `institutional_data/` supplies the hard numbers (admit rates, trends, lawsuit disclosures, legal/policy structure) that every qualitative claim in `qualitative_insights/` should be checked against. `pipeline/` holds the scraper and its checkpoint state, kept separate from the data it produces.

**Adding new files:** place them in the matching category folder rather than at root. Internal relative-path references between files (e.g. a reference doc in `institutional_data/` pointing at `school_data/...`) rely on the referenced folder being a sibling — keep data folders alongside the `.md` files that cite them if either ever moves again.
