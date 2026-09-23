import urllib.request, urllib.parse, json, time

ANON = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImlzZHV3bXlndm1kb3pocHZ6YWl4Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzYxMDk3NTksImV4cCI6MjA5MTY4NTc1OX0.fYZOIHyrOWzidgc-CVxWCY5Fe9pQk12-6YjDIS6y9qs"
BASE = "https://api.collegedata.fyi/rest/v1/ipeds_facts"
FIELDS = ["admit_rate_total", "applicants_total", "admissions_total", "enrolled_total",
          "sat_ebrw_p25", "sat_ebrw_p50", "sat_ebrw_p75",
          "sat_math_p25", "sat_math_p50", "sat_math_p75",
          "act_composite_p25", "act_composite_p50", "act_composite_p75",
          "sat_submit_rate", "act_submit_rate", "yield_rate_total",
          "retention_rate_full_time", "bachelor_6yr_grad_rate"]

def get(u):
    req = urllib.request.Request(u, headers={"apikey": ANON, "Authorization": f"Bearer {ANON}",
                                              "X-CollegeData-Client": "personal-research-script"})
    return json.loads(urllib.request.urlopen(req, timeout=60).read().decode())

ipeds_ids = json.load(open("ipeds_ids.json"))
out = {}
miss = []
field_list = ",".join(FIELDS)
for name, iid in ipeds_ids.items():
    try:
        url = (f"{BASE}?ipeds_id=eq.{iid}&field_key=in.({field_list})"
               f"&select=data_year,field_key,value_numeric&order=data_year.asc&limit=1000")
        rows = get(url)
        by_year = {}
        for r in rows:
            y = r["data_year"]
            by_year.setdefault(y, {})[r["field_key"]] = r["value_numeric"]
        out[name] = {"ipeds_id": iid, "years": by_year}
    except Exception as e:
        miss.append(f"{name} ERR {str(e)[:80]}")
    time.sleep(0.3)

json.dump(out, open("ipeds_trends_raw.json", "w"), indent=1)
print(len(out), "schools fetched;", len(miss), "missed")
for m in miss:
    print(" ", m)
