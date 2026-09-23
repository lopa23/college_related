import json
facts=json.load(open("cds_facts_raw.json")); secc=json.load(open("cds_section_c.json"))
C7={701:"rigor",702:"class_rank",703:"gpa",704:"test_scores",705:"essay",706:"recommendations",707:"interview",708:"extracurriculars",709:"talent",710:"character",711:"first_gen",712:"legacy",713:"geography",714:"state_residency",715:"religion",716:"volunteer",717:"work_experience",718:"demonstrated_interest"}
def fv(f,key):
    for x in f:
        if x["key"]==key: return x["value"]
def num(x):
    try: return float(x)
    except: return None
out={}
for n,v in facts.items():
    f=v["facts"]; rows=secc[n]["rows"]
    years=sorted({r["canonical_year"] for r in rows}); latest=years[-1] if years else None
    lr=[r for r in rows if r["canonical_year"]==latest]
    c7={}
    for r in lr:
        try: k=int(r["field_id"].split(".")[1])
        except: continue
        if k in C7 and r["value_text"] in ("Very Important","Important","Considered","Not Considered"): c7[C7[k]]=r["value_text"]
    def cf(fid):
        for r in lr:
            if r["field_id"]==fid: return num(r["value_num"] if r["value_num"] is not None else r["value_text"])
    gpa=cf("C.1201"); gpa=gpa if gpa and 2<gpa<=5 else None
    tenth=cf("C.1121"); tenth=tenth if tenth and 0<tenth<=100 else None
    ed_app,ed_adm=fv(f,"ed_applicants"),fv(f,"ed_admitted")
    ar=fv(f,"ipeds.admit_rate_total")
    out[n]={"school_id":v["school_id"],"cds_year":latest,
     "admit_rate_ipeds":ar,"applicants":fv(f,"ipeds.applicants_total"),
     "sat_ebrw":[fv(f,"ipeds.sat_ebrw_p25"),fv(f,"ipeds.sat_ebrw_p50"),fv(f,"ipeds.sat_ebrw_p75")],
     "sat_math":[fv(f,"ipeds.sat_math_p25"),fv(f,"ipeds.sat_math_p50"),fv(f,"ipeds.sat_math_p75")],
     "act":[fv(f,"ipeds.act_composite_p25"),fv(f,"ipeds.act_composite_p50"),fv(f,"ipeds.act_composite_p75")],
     "sat_submit_rate":fv(f,"ipeds.sat_submit_rate"),"act_submit_rate":fv(f,"ipeds.act_submit_rate"),
     "ed_offered":fv(f,"ed_offered"),"ea_offered":fv(f,"ea_offered"),
     "ed_applicants":ed_app,"ed_admitted":ed_adm,"ed_admit_rate":(round(ed_adm/ed_app,3) if ed_app and ed_adm and ed_app>0 and ed_adm<=ed_app else None),
     "yield":fv(f,"ipeds.yield_rate_total"),
     "avg_gpa_admitted":gpa,"pct_top_tenth":tenth,"c7_factors":c7,
     "avg_net_price":fv(f,"avg_net_price"),"net_price_0_30k":fv(f,"net_price_0_30k"),
     "grad_rate_6yr":fv(f,"graduation_rate_6yr"),"earnings_10yr_median":fv(f,"earnings_10yr_median"),"median_debt":fv(f,"median_debt_completers"),
     "source":"collegedata.fyi (CDS + IPEDS extraction; verify against school's own CDS before citing)"}
json.dump(out,open("school_facts.json","w"),indent=1)
print(len(out), "schools;", sum(1 for v in out.values() if v["c7_factors"]),"with C7;", sum(1 for v in out.values() if v["avg_gpa_admitted"]),"with GPA")
for n in ["Massachusetts Institute of Technology","Stanford University","University of Illinois Urbana-Champaign","Georgia Institute of Technology"]:
    v=out[n]; print(n, v["admit_rate_ipeds"], v["sat_math"], v["ed_admit_rate"], v["c7_factors"].get("demonstrated_interest"), v["avg_gpa_admitted"])
