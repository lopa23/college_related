import urllib.request, urllib.parse, json, time

# Set to a personal key from https://api.data.gov/signup/ to avoid the shared
# DEMO_KEY's low global rate limit (DEMO_KEY is shared across all unauthenticated
# callers everywhere, so its quota can stay exhausted regardless of local waiting).
KEY = "DEMO_KEY"

FIELDS = [
    "id", "school.name", "school.city", "school.state",
    "latest.student.size",
    "latest.admissions.admission_rate.overall",
    "latest.student.demographics.race_ethnicity.white",
    "latest.student.demographics.race_ethnicity.black",
    "latest.student.demographics.race_ethnicity.hispanic",
    "latest.student.demographics.race_ethnicity.asian",
    "latest.student.demographics.race_ethnicity.aian",
    "latest.student.demographics.race_ethnicity.nhpi",
    "latest.student.demographics.race_ethnicity.two_or_more",
    "latest.student.demographics.race_ethnicity.non_resident_alien",
    "latest.student.demographics.race_ethnicity.unknown",
    "latest.student.demographics.men",
    "latest.student.demographics.women",
    "latest.student.demographics.age_entry",
    "latest.student.share_firstgeneration",
    "latest.aid.pell_grant_rate",
    "latest.academics.program_percentage.computer",
    "latest.academics.program_percentage.engineering",
    "latest.academics.program_percentage.biological",
    "latest.academics.program_percentage.business_marketing",
    "latest.academics.program_percentage.social_science",
    "latest.academics.program_percentage.psychology",
    "latest.academics.program_percentage.health",
    "latest.academics.program_percentage.visual_performing",
    "latest.academics.program_percentage.communication",
    "latest.academics.program_percentage.english",
    "latest.academics.program_percentage.mathematics",
    "latest.academics.program_percentage.physical_science",
    "latest.academics.program_percentage.history",
    "latest.academics.program_percentage.multidiscipline",
    "latest.academics.program_percentage.public_administration_social_service",
]

TOP20 = [
    "Princeton University", "Massachusetts Institute of Technology", "Harvard University",
    "Stanford University", "Yale University", "University of Pennsylvania",
    "California Institute of Technology", "Duke University", "Brown University",
    "Johns Hopkins University", "Northwestern University",
    "Columbia University in the City of New York", "Cornell University",
    "University of Chicago", "University of California-Los Angeles",
    "University of California-Berkeley", "Rice University", "University of Notre Dame",
    "Vanderbilt University", "University of Michigan-Ann Arbor",
]

out = json.load(open("scorecard_demographics_top20.json", encoding="utf-8"))
missing = [n for n in TOP20 if n not in out]
print("missing:", missing)

for name in missing:
    q = urllib.parse.urlencode({"api_key": KEY, "school.name": name, "fields": ",".join(FIELDS)})
    url = "https://api.data.gov/ed/collegescorecard/v1/schools.json?" + q
    d = None
    err = None
    for attempt in range(4):
        try:
            d = json.load(urllib.request.urlopen(url, timeout=40))
            break
        except Exception as e:
            err = e
            time.sleep(20)
    if not d or not d.get("results"):
        print("MISS", name, "err=", err)
        continue
    res = d["results"]
    exact = [r for r in res if r["school.name"] == name] or res
    out[name] = exact[0]
    print("OK", name)
    time.sleep(20)

json.dump(out, open("scorecard_demographics_top20.json", "w"), indent=1)
print(len(out), "schools total")
