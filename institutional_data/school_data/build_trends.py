import json

raw = json.load(open("ipeds_trends_raw.json"))

def latest_nonnull(years, key, before=None):
    yrs = sorted((int(y) for y in years.keys()), reverse=True)
    for y in yrs:
        if before and y >= before:
            continue
        v = years[str(y)].get(key)
        if v is not None:
            return y, v
    return None, None

def earliest_nonnull(years, key, after=2013):
    yrs = sorted(int(y) for y in years.keys())
    for y in yrs:
        if y < after:
            continue
        v = years[str(y)].get(key)
        if v is not None:
            return y, v
    return None, None

out = {}
for name, v in raw.items():
    years = v["years"]
    y0, ar0 = earliest_nonnull(years, "admit_rate_total")
    y1, ar1 = latest_nonnull(years, "admit_rate_total")
    _, app0 = (y0, years.get(str(y0), {}).get("applicants_total")) if y0 else (None, None)
    _, app1 = (y1, years.get(str(y1), {}).get("applicants_total")) if y1 else (None, None)
    _, yield0 = (y0, years.get(str(y0), {}).get("yield_rate_total")) if y0 else (None, None)
    _, yield1 = (y1, years.get(str(y1), {}).get("yield_rate_total")) if y1 else (None, None)
    _, sat0 = (y0, years.get(str(y0), {}).get("sat_ebrw_p50")) if y0 else (None, None)
    _, sat1 = (y1, years.get(str(y1), {}).get("sat_ebrw_p50")) if y1 else (None, None)
    m0 = years.get(str(y0), {}).get("sat_math_p50") if y0 else None
    m1 = years.get(str(y1), {}).get("sat_math_p50") if y1 else None
    satsum0 = (sat0 + m0) if (sat0 is not None and m0 is not None) else None
    satsum1 = (sat1 + m1) if (sat1 is not None and m1 is not None) else None
    out[name] = {
        "ipeds_id": v["ipeds_id"],
        "start_year": y0, "end_year": y1,
        "admit_rate_start": ar0, "admit_rate_end": ar1,
        "admit_rate_pt_change": (round(ar1 - ar0, 1) if ar0 is not None and ar1 is not None else None),
        "applicants_start": app0, "applicants_end": app1,
        "applicants_pct_change": (round((app1 - app0) / app0 * 100, 1) if app0 and app1 else None),
        "yield_start": yield0, "yield_end": yield1,
        "sat_total_p50_start": satsum0, "sat_total_p50_end": satsum1,
        "full_series": {y: {"admit_rate": years[y].get("admit_rate_total"),
                             "applicants": years[y].get("applicants_total"),
                             "yield": years[y].get("yield_rate_total"),
                             "sat_ebrw_p50": years[y].get("sat_ebrw_p50"),
                             "sat_math_p50": years[y].get("sat_math_p50"),
                             "act_composite_p50": years[y].get("act_composite_p50")}
                        for y in sorted(years.keys()) if int(y) >= 2014}
    }

json.dump(out, open("school_admit_trends.json", "w"), indent=1)

ranked = sorted((v for v in out.values() if v["admit_rate_pt_change"] is not None),
                key=lambda v: v["admit_rate_pt_change"])
print(f"{len(out)} schools processed, {len(ranked)} with a computable admit-rate trend\n")
print(f"{'School':45} {'Start':>6} {'End':>6} {'Change':>8}  {'Applicants % chg':>17}")
name_by_id = {v["ipeds_id"]: n for n, v in out.items()}
for n, v in sorted(out.items(), key=lambda kv: (kv[1]["admit_rate_pt_change"] if kv[1]["admit_rate_pt_change"] is not None else 999)):
    if v["admit_rate_pt_change"] is None:
        continue
    print(f"{n[:45]:45} {v['admit_rate_start']:>5}% {v['admit_rate_end']:>5}% {v['admit_rate_pt_change']:>+7.1f}pt  {v['applicants_pct_change']:>+15.1f}%" if v["applicants_pct_change"] is not None else f"{n[:45]:45} {v['admit_rate_start']:>5}% {v['admit_rate_end']:>5}% {v['admit_rate_pt_change']:>+7.1f}pt")
