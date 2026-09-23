# -*- coding: utf-8 -*-
# Consolidates raw IPEDS complete-data-files (ADM, EF-D retention, C_A completions,
# HD directory) into three compact per-year long-format CSVs covering all
# Title-IV institutions, 2014-2023. Source: nces.ed.gov/ipeds/datacenter/data/*.zip
import csv, glob, os, re

os.chdir(os.path.dirname(os.path.abspath(__file__)) + "/unzipped")

def num(x):
    try:
        v = float(x)
        return v
    except (TypeError, ValueError):
        return None

def rows_for(prefix, year):
    rv = f"{prefix}{year}_rv.csv"
    base = f"{prefix}{year}.csv"
    fn = rv if os.path.exists(rv) else base
    if not os.path.exists(fn):
        # try lowercase variants already normalized; also try without rv suffix casing issues
        cands = glob.glob(f"{prefix}{year}*.csv")
        fn = cands[0] if cands else None
    if not fn:
        return []
    with open(fn, newline="", encoding="utf-8-sig") as f:
        return list(csv.DictReader(f))

# --- 1. Institution directory (name, state, sector) ---
directory = {}
for r in rows_for("hd", 2023):
    directory[r["UNITID"]] = {"name": r.get("INSTNM"), "state": r.get("STABBR"),
                                "city": r.get("CITY"), "sector": r.get("SECTOR")}

# --- 2. Admissions trend (applicants, admits, enrolled, SAT/ACT medians) ---
with open("../national_admissions_trends.csv", "w", newline="", encoding="utf-8") as out:
    w = csv.writer(out)
    w.writerow(["unitid", "year", "institution", "state", "applicants", "admitted", "enrolled",
                "admit_rate_pct", "yield_rate_pct", "sat_ebrw_p50", "sat_math_p50", "act_composite_p50"])
    for year in range(2014, 2024):
        for r in rows_for("adm", year):
            uid = r["UNITID"]
            app, adm, enr = num(r.get("APPLCN")), num(r.get("ADMSSN")), num(r.get("ENRLT"))
            admit_rate = round(adm / app * 100, 1) if app and adm and app > 0 else None
            yield_rate = round(enr / adm * 100, 1) if adm and enr and adm > 0 else None
            info = directory.get(uid, {})
            w.writerow([uid, year, info.get("name"), info.get("state"), app, adm, enr,
                        admit_rate, yield_rate,
                        num(r.get("SATVR50")), num(r.get("SATMT50")), num(r.get("ACTCM50"))])

# --- 3. Retention trend ---
with open("../national_retention_trends.csv", "w", newline="", encoding="utf-8") as out:
    w = csv.writer(out)
    w.writerow(["unitid", "year", "institution", "state", "cohort_size_full_time",
                "retention_rate_full_time_pct", "retention_rate_part_time_pct"])
    for year in range(2014, 2024):
        for r in rows_for("ef", str(year) + "d") or rows_for("ef", f"{year}d"):
            uid = r["UNITID"]
            info = directory.get(uid, {})
            w.writerow([uid, year, info.get("name"), info.get("state"),
                        num(r.get("GRCOHRT")), num(r.get("RET_PCF")), num(r.get("RET_PCP"))])

# --- 4. Completions trend (total awarded degrees per institution per year, all CIP/levels summed, MAJORNUM=1 only to avoid double-counting double majors) ---
with open("../national_completions_trends.csv", "w", newline="", encoding="utf-8") as out:
    w = csv.writer(out)
    w.writerow(["unitid", "year", "institution", "state", "total_completions"])
    for year in range(2014, 2024):
        totals = {}
        for r in rows_for("c", str(year) + "_a") or rows_for("c", f"{year}_a"):
            if r.get("MAJORNUM") != "1":
                continue
            uid = r["UNITID"]
            v = num(r.get("CTOTALT")) or 0
            totals[uid] = totals.get(uid, 0) + v
        for uid, total in totals.items():
            info = directory.get(uid, {})
            w.writerow([uid, year, info.get("name"), info.get("state"), total])

print("Done. Wrote national_admissions_trends.csv, national_retention_trends.csv, national_completions_trends.csv")
