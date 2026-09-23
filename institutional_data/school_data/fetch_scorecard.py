import urllib.request, urllib.parse, json, time
KEY="DEMO_KEY"
schools = ["Massachusetts Institute of Technology","Stanford University","Carnegie Mellon University","University of California-Berkeley","California Institute of Technology","Georgia Institute of Technology-Main Campus","University of Illinois Urbana-Champaign","Cornell University","Princeton University","University of Michigan-Ann Arbor","The University of Texas at Austin","University of Washington-Seattle Campus","Purdue University-Main Campus","Harvard University","Yale University","University of Pennsylvania","Columbia University in the City of New York","Duke University","Northwestern University","Johns Hopkins University","Dartmouth College","Brown University","Vanderbilt University","Rice University","University of Notre Dame","University of Chicago","University of California-Los Angeles","University of California-San Diego","University of California-Santa Barbara","University of California-Irvine","University of California-Davis","University of Wisconsin-Madison","University of Maryland-College Park","Virginia Polytechnic Institute and State University","Northeastern University","University of Southern California","New York University","Washington University in St Louis","Emory University","University of Virginia-Main Campus","University of North Carolina at Chapel Hill","Boston University","Case Western Reserve University","Rensselaer Polytechnic Institute","Worcester Polytechnic Institute","Harvey Mudd College","University of Rochester","Tufts University","Georgetown University","University of Florida","Texas A & M University-College Station","Ohio State University-Main Campus","University at Buffalo","Rutgers University-New Brunswick","University of Minnesota-Twin Cities","Pennsylvania State University-Main Campus","Olin College of Engineering","Rose-Hulman Institute of Technology","University of California-San Diego","California Polytechnic State University-San Luis Obispo"]
fields = ["id","school.name","school.city","school.state","school.ownership","latest.student.size",
"latest.admissions.admission_rate.overall",
"latest.admissions.sat_scores.25th_percentile.critical_reading","latest.admissions.sat_scores.75th_percentile.critical_reading",
"latest.admissions.sat_scores.25th_percentile.math","latest.admissions.sat_scores.75th_percentile.math",
"latest.admissions.act_scores.25th_percentile.cumulative","latest.admissions.act_scores.75th_percentile.cumulative",
"latest.admissions.test_requirements",
"latest.cost.avg_net_price.overall","latest.cost.net_price.public.by_income_level.0-30000","latest.cost.net_price.public.by_income_level.30001-48000","latest.cost.net_price.public.by_income_level.48001-75000","latest.cost.net_price.public.by_income_level.75001-110000","latest.cost.net_price.public.by_income_level.110001-plus",
"latest.cost.net_price.private.by_income_level.0-30000","latest.cost.net_price.private.by_income_level.30001-48000","latest.cost.net_price.private.by_income_level.48001-75000","latest.cost.net_price.private.by_income_level.75001-110000","latest.cost.net_price.private.by_income_level.110001-plus",
"latest.completion.consumer_rate","latest.earnings.10_yr.median","latest.student.demographics.first_generation","latest.student.share_firstgeneration","latest.aid.pell_grant_rate"]
out={}
for s in dict.fromkeys(schools):
    q=urllib.parse.urlencode({"api_key":KEY,"school.name":s,"fields":",".join(fields)})
    url="https://api.data.gov/ed/collegescorecard/v1/schools.json?"+q
    for attempt in range(3):
        try:
            d=json.load(urllib.request.urlopen(url,timeout=40)); break
        except Exception as e:
            d=None; time.sleep(3)
    if not d or not d.get("results"): print("MISS",s); continue
    res=d["results"]
    exact=[r for r in res if r["school.name"]==s] or res
    out[s]=exact[0]; time.sleep(0.5)
json.dump(out,open("scorecard_raw.json","w"),indent=1)
print(len(out),"schools")
