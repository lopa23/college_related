# National IPEDS trend data (2014–2023, ~2,000 institutions)

Raw source: [NCES IPEDS Data Center complete data files](https://nces.ed.gov/ipeds/use-the-data), `https://nces.ed.gov/ipeds/datacenter/data/{COMPONENT}{YEAR}.zip`. This is the *entire* national IPEDS admissions/enrollment/completions record — every Title-IV institution, not just the 60-school curated set used elsewhere in this project (`school_data/school_facts.json`, `school_admit_trends.json`). Use this when a question needs a peer group outside the 60-school list, or true national base rates.

## Files

- **`raw/`** — the original downloaded zips, one per component per year: `ADM{year}.zip` (Admissions & Test Scores), `EF{year}D.zip` (Fall Enrollment, Part D = retention rates), `C{year}_A.zip` (Completions, Part A), plus `HD2023.zip` (institution directory: name/state/city/sector, used once to label all years). 2014–2023 is the most recent 10-year window available (Fall 2024/2025 admissions data isn't in IPEDS yet as of this pull). Re-unzip with any zip tool; each contains a raw CSV plus a `_Dict` metadata file describing every column.
- **`national_admissions_trends.csv`** — one row per institution per year: `unitid, year, institution, state, applicants, admitted, enrolled, admit_rate_pct, yield_rate_pct, sat_ebrw_p50, sat_math_p50, act_composite_p50`. ~1,970–2,060 institutions per year, 2014–2023.
- **`national_retention_trends.csv`** — one row per institution per year: `unitid, year, institution, state, cohort_size_full_time, retention_rate_full_time_pct, retention_rate_part_time_pct`.
- **`national_completions_trends.csv`** — one row per institution per year: `unitid, year, institution, state, total_completions` (sum of `CTOTALT` across all CIP codes/award levels for `MAJORNUM=1` rows only, to avoid double-counting students with a declared double major — this is total *degrees conferred* that year, all levels combined, not just bachelor's).

Join key across all three, and against `school_facts.json`'s IPEDS-derived fields, is `unitid` (= IPEDS `UNITID`, a stable federal institution ID — not the same as `school_id` used in the CDS-derived files elsewhere in this project).

## Known gaps

- SAT/ACT median columns are empty for many institution-years in the earlier part of the window (roughly pre-2022) — this reflects real IPEDS data collection changes around test-optional policies, not a processing error; don't treat a blank as zero.
- `total_completions` sums every award level (certificates through doctorates) — if you need bachelor's-only, re-derive from the raw `C{year}_A` files' `AWLEVEL` column (bachelor's = code 5) rather than trusting the pre-summed column here.
- This is federal IPEDS `admit_rate_total`/`ADMSSN`/`APPLCN` methodology — whole-institution, not program-level. It will not match §4's program-level CS/Engineering admit rates in the main reference doc.

## Reproducing or extending

`build_national_trends.py` regenerates the three CSVs from `raw/`. To add more years or components (e.g. full Fall Enrollment demographic breakdown, not just retention), download `https://nces.ed.gov/ipeds/datacenter/data/{COMPONENT}{YEAR}.zip` for the desired component/year into `raw/`, unzip into a `unzipped/` folder (git-ignored/deleted after each run to save space — the 10-year, 3-component unzip was ~1.2GB), and extend the script's `rows_for()` calls. No API key or auth needed; it's a public, unauthenticated federal file server.
