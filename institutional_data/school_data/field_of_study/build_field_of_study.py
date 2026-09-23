# -*- coding: utf-8 -*-
# Extracts bachelor's-degree-level earnings/debt data for Computer Science and
# Engineering CIP codes from the College Scorecard's national Field-of-Study file.
# Source: https://collegescorecard.ed.gov/data/ -> "Most Recent Cohorts: Field of Study"
import csv

TARGET_CIP_PREFIXES = {
    "11": "Computer and Information Sciences",
    "14": "Engineering",
}
BACHELOR_CREDLEV = "3"

def num(x):
    try:
        return float(x)
    except (TypeError, ValueError):
        return None  # covers "PS" (privacy-suppressed) and blanks

rows_out = []
with open("fos_temp/Most-Recent-Cohorts-Field-of-Study.csv", encoding="utf-8-sig") as f:
    r = csv.DictReader(f)
    for row in r:
        if row["CREDLEV"] != BACHELOR_CREDLEV:
            continue
        cip2 = row["CIPCODE"][:2]
        if cip2 not in TARGET_CIP_PREFIXES:
            continue
        rows_out.append({
            "unitid": row["UNITID"],
            "institution": row["INSTNM"],
            "cip_code": row["CIPCODE"],
            "field": row["CIPDESC"].strip().rstrip("."),
            "earnings_median_1yr": num(row.get("EARN_MDN_HI_1YR")),
            "earnings_median_2yr": num(row.get("EARN_MDN_HI_2YR")),
            "earnings_count_1yr": num(row.get("EARN_COUNT_WNE_HI_1YR")),
            "median_debt": num(row.get("DEBT_ALL_STGP_ANY_MDN")),
            "completers_ipeds": num(row.get("IPEDSCOUNT1")),
        })

with open("national_cs_engineering_earnings.csv", "w", newline="", encoding="utf-8") as out:
    w = csv.DictWriter(out, fieldnames=list(rows_out[0].keys()))
    w.writeheader()
    w.writerows(rows_out)

with_earnings = [r for r in rows_out if r["earnings_median_1yr"] is not None]
print(f"{len(rows_out)} bachelor's-level CS/Engineering program rows across all institutions")
print(f"{len(with_earnings)} have non-suppressed 1-year earnings data")

# Quick sanity check: top 15 by 1-year earnings among rows with a decent sample size
ranked = sorted((r for r in with_earnings if (r["earnings_count_1yr"] or 0) >= 30),
                key=lambda r: -r["earnings_median_1yr"])
print("\nTop 15 CS/Engineering bachelor's programs by 1-year median earnings (n>=30):")
for r in ranked[:15]:
    print(f"  {r['institution'][:45]:45} {r['field'][:30]:30} ${r['earnings_median_1yr']:>9,.0f}  n={r['earnings_count_1yr']:.0f}")
