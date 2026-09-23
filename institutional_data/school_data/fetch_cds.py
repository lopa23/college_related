import urllib.request, urllib.parse, json, time, re
def get(u):
    req=urllib.request.Request(u,headers={"X-CollegeData-Client":"personal-research-script","User-Agent":"Mozilla/5.0"})
    return json.loads(urllib.request.urlopen(req,timeout=60).read().decode())
names=["Massachusetts Institute of Technology","Stanford University","Carnegie Mellon University","University of California, Berkeley","California Institute of Technology","Georgia Institute of Technology","University of Illinois Urbana-Champaign","Cornell University","Princeton University","University of Michigan","University of Texas at Austin","University of Washington","Purdue University","Harvard University","Yale University","University of Pennsylvania","Columbia University","Duke University","Northwestern University","Johns Hopkins University","Dartmouth College","Brown University","Vanderbilt University","Rice University","University of Notre Dame","University of Chicago","University of California, Los Angeles","University of California, San Diego","University of California, Santa Barbara","University of California, Irvine","University of California, Davis","University of Wisconsin-Madison","University of Maryland, College Park","Virginia Tech","Northeastern University","University of Southern California","New York University","Washington University in St. Louis","Emory University","University of Virginia","University of North Carolina at Chapel Hill","Boston University","Case Western Reserve University","Rensselaer Polytechnic Institute","Worcester Polytechnic Institute","Harvey Mudd College","University of Rochester","Tufts University","Georgetown University","University of Florida","Texas A&M University","Ohio State University","University at Buffalo","Rutgers University","University of Minnesota","Penn State","Olin College","Rose-Hulman","Cal Poly San Luis Obispo","Wake Forest","Swarthmore"]
out={}; miss=[]
for n in names:
    try:
        r=get("https://www.collegedata.fyi/api/schools/search?q="+urllib.parse.quote(n))["results"]
        if not r: miss.append(n); continue
        sid=r[0]["school_id"]
        f=get(f"https://www.collegedata.fyi/api/schools/{sid}/facts?categories=admissions,cost,outcomes,finance")
        out[n]={"school_id":sid,"matched":r[0]["school_name"],"facts":f["facts"]}
    except Exception as e:
        miss.append(n+" ERR "+str(e)[:60])
    time.sleep(0.4)
json.dump(out,open("cds_facts_raw.json","w"),indent=1)
print(len(out),"ok; miss:",miss)
