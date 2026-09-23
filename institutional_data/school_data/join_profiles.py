import json, re
P="combined_profiles.json"
prof=json.load(open(P,encoding="utf-8")); facts=json.load(open("school_data/school_facts.json"))
A=[ # (canonical, regex) ordered: specific first
("Massachusetts Institute of Technology",r"\bMIT\b|Massachusetts Institute"),
("Stanford University",r"Stanford"),
("Carnegie Mellon University",r"Carnegie Mellon|\bCMU\b"),
("California Institute of Technology",r"Caltech|California Institute of Tech"),
("Georgia Institute of Technology",r"Georgia Tech|Georgia Institute"),
("University of Illinois Urbana-Champaign",r"UIUC|Illinois Urbana|University of Illinois(?! at Chicago| Chicago)|\bUIUC\b"),
("Cornell University",r"Cornell(?! College)"),
("Princeton University",r"Princeton"),
("University of California, Berkeley",r"UC Berkeley|UCB\b|Berkeley|Cal Berkeley"),
("University of California, Los Angeles",r"UCLA|UC Los Angeles"),
("University of California, San Diego",r"UCSD|UC San Diego"),
("University of California, Santa Barbara",r"UCSB|UC Santa Barbara"),
("University of California, Irvine",r"UCI\b|UC Irvine"),
("University of California, Davis",r"UC Davis|UCD\b"),
("University of Michigan",r"(?<!Central )(?<!Eastern )(?<!Western )(?<!Northern )University of Michigan(?!.{0,3}(Dearborn|Flint))|\bUMich\b|\bU-?M\b Ann Arbor|Michigan(?! State)(?! Tech)"),
("University of Texas at Austin",r"UT Austin|University of Texas(?: at|,)? Austin"),
("University of Washington",r"University of Washington|\bUW Seattle|\bUW-Seattle"),
("Purdue University",r"Purdue"),
("Harvard University",r"Harvard"),
("Yale University",r"\bYale"),
("University of Pennsylvania",r"UPenn|U Penn|University of Pennsylvania|\bPenn\b(?! State)"),
("Columbia University",r"Columbia(?! College Chicago)(?! University Chicago)"),
("Duke University",r"\bDuke"),
("Northwestern University",r"Northwestern"),
("Johns Hopkins University",r"Johns Hopkins|\bJHU\b"),
("Dartmouth College",r"Dartmouth"),
("Brown University",r"Brown University|\bBrown\b"),
("Vanderbilt University",r"Vanderbilt|\bVandy\b"),
("Rice University",r"\bRice\b"),
("University of Notre Dame",r"Notre Dame"),
("University of Chicago",r"UChicago|University of Chicago"),
("University of Wisconsin-Madison",r"Wisconsin"),
("University of Maryland, College Park",r"University of Maryland|\bUMD\b|Maryland,? College Park"),
("Virginia Tech",r"Virginia Tech|\bVT\b"),
("Northeastern University",r"Northeastern"),
("University of Southern California",r"\bUSC\b|Southern California"),
("New York University",r"\bNYU\b|New York University"),
("Washington University in St. Louis",r"WashU|Washington University|WUSTL"),
("Emory University",r"Emory"),
("University of Virginia",r"\bUVA\b|University of Virginia"),
("University of North Carolina at Chapel Hill",r"UNC|Chapel Hill"),
("Boston University",r"Boston University|\bBU\b"),
("Case Western Reserve University",r"Case Western|\bCWRU\b"),
("Rensselaer Polytechnic Institute",r"\bRPI\b|Rensselaer"),
("Worcester Polytechnic Institute",r"\bWPI\b|Worcester Polytechnic"),
("Harvey Mudd College",r"Harvey Mudd"),
("University of Rochester",r"University of Rochester"),
("Tufts University",r"Tufts"),
("Georgetown University",r"Georgetown"),
("University of Florida",r"University of Florida|\bUF\b"),
("Texas A&M University",r"Texas A&M|Texas A&amp;M|\bTAMU\b"),
("Ohio State University",r"Ohio State|\bOSU\b"),
("University at Buffalo",r"University at Buffalo|Buffalo"),
("Rutgers University",r"Rutgers"),
("University of Minnesota",r"University of Minnesota|Minnesota Twin"),
("Penn State",r"Penn State|Pennsylvania State"),
("Wake Forest",r"Wake Forest"),("Swarthmore",r"Swarthmore"),
]
NAMEMAP={n:n for n in facts}
skip=re.compile(r"^\W*(undetermined|undecided|rejected|deferred|declined|not (fully )?(stated|confirmed|clear)|n/?a|ambiguous|leaning|unclear|unknown|tbd|still|pending|no |none|likely|probably|possibly|weighing|deciding)",re.I)
def find_school(text):
    best=None
    for canon,rx in A:
        if canon not in facts: continue
        m=re.search(rx,text)
        if m and (best is None or m.start()<best[0]): best=(m.start(),canon)
    return best[1] if best else None
def parse_sat(t):
    m=re.search(r"SAT[^0-9]{0,25}((?:1[0-6]\d0|[5-9]\d0))",t or "")
    if m and len(m.group(1))==4: return int(m.group(1))
def parse_act(t):
    m=re.search(r"ACT[^0-9]{0,20}(3[0-6]|2\d)\b",t or "")
    return int(m.group(1)) if m else None
matched=unmatched=skipped=0; pos={"below_p25":0,"within":0,"above_p75":0}
for k,v in prof.items():
    v.pop("school_context",None)
    ct=v.get("committed_to") or ""
    if not ct or skip.search(ct): skipped+=1; continue
    canon=find_school(ct)
    if not canon: unmatched+=1; continue
    f=facts[canon]; matched+=1
    ctx={"school":canon,"cds_year":f["cds_year"],"admit_rate_pct":f["admit_rate_ipeds"],"c7_demonstrated_interest":f["c7_factors"].get("demonstrated_interest"),"c7_legacy":f["c7_factors"].get("legacy"),"ed_admit_rate":f["ed_admit_rate"],"avg_gpa_admitted":f["avg_gpa_admitted"]}
    e,m_=f["sat_ebrw"],f["sat_math"]
    txt=" ".join(str(v.get(x) or "") for x in ("gpa","note","honors_awards"))
    sat=parse_sat(txt)
    try: lo,hi=e[0]+m_[0],e[2]+m_[2]
    except: lo=hi=None
    if sat and lo:
        ctx["applicant_sat"]=sat; ctx["school_sat_approx_range"]=[lo,hi]
        c="below_p25" if sat<lo else "above_p75" if sat>hi else "within"
        ctx["sat_position"]=c; pos[c]+=1
    act=parse_act(txt)
    if act and f["act"][0]:
        ctx["applicant_act"]=act; ctx["school_act_range"]=[f["act"][0],f["act"][2]]
    v["school_context"]=ctx
json.dump(prof,open(P,"w",indent=2,ensure_ascii=False),ensure_ascii=False) if False else json.dump(prof,open(P,"w",encoding="utf-8"),indent=2,ensure_ascii=False)
print("matched",matched,"unmatched(school not in 60-list or unparsed)",unmatched,"skipped(no commit)",skipped,"total",len(prof)); print(pos)
