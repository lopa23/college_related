# Finds YouTube videos for college-counseling queries by parsing YouTube search result pages (stdlib only)
# and records them in youtube_videos.db (status='discovered').
import urllib.request, urllib.parse, json, re, sqlite3, time, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
DB = os.path.join(HERE, "youtube_videos.db")

QUERIES = [
    "college admissions officer explains how applications are read",
    "former admissions officer advice college applications",
    "how to write the common app essay admissions officer",
    "college essay tips admissions dean",
    "supplemental essay why us tips admissions",
    "college counselor advice building a college list",
    "how to build a college list reach target safety",
    "early decision vs early action strategy",
    "test optional vs submit SAT strategy admissions officer",
    "extracurricular activities colleges want admissions officer",
    "common app activities list tips",
    "letters of recommendation college admissions tips",
    "college interview tips admissions",
    "financial aid and scholarships explained college counselor",
    "FAFSA CSS profile explained",
    "college admissions myths debunked",
    "holistic review explained college admissions",
    "college admissions for computer science majors",
    "how to get into MIT admissions advice",
    "how to get into Stanford admissions officer",
    "how to get into Ivy League admissions officer insight",
    "college admissions webinar admissions office",
    "Yale admissions office podcast",
    "admissions beat podcast Dartmouth",
    "waitlist deferral what to do college admissions",
    "college admissions freshman year high school plan",
    "AP courses rigor college admissions counselor",
    "demonstrated interest college admissions",
    "first generation college applicant advice counselor",
    "international students US college admissions advice",
    "STEM research summer programs college admissions",
    "college admissions trends this year counselor",
    "Common App personal statement examples analysis",
    "how colleges evaluate GPA and course rigor",
    "college admissions counselor Q&A live",
]

def db():
    c = sqlite3.connect(DB)
    c.executescript(open(os.path.join(HERE, "schema.sql")).read())
    return c

def search(q):
    url = "https://www.youtube.com/results?search_query=" + urllib.parse.quote(q) + "&sp=EgIQAQ%253D%253D"
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0", "Accept-Language": "en-US,en;q=0.9"})
    html = urllib.request.urlopen(req, timeout=30).read().decode("utf8", "ignore")
    m = re.search(r"var ytInitialData = (\{.*?\});</script>", html, re.S)
    if not m:
        return []
    data = json.loads(m.group(1))
    out = []
    def walk(o):
        if isinstance(o, dict):
            if "videoRenderer" in o:
                v = o["videoRenderer"]
                vid = v.get("videoId")
                title = "".join(r.get("text", "") for r in v.get("title", {}).get("runs", []))
                chan = "".join(r.get("text", "") for r in v.get("ownerText", {}).get("runs", []))
                length = v.get("lengthText", {}).get("simpleText")
                views = v.get("viewCountText", {}).get("simpleText")
                pub = v.get("publishedTimeText", {}).get("simpleText")
                if vid:
                    out.append((vid, title, chan, length, views, pub))
            for x in o.values():
                walk(x)
        elif isinstance(o, list):
            for x in o:
                walk(x)
    walk(data)
    return out

if __name__ == "__main__":
    c = db()
    new = 0
    for q in QUERIES:
        try:
            res = search(q)
        except Exception as e:
            print("ERR", q, str(e)[:80]); time.sleep(3); continue
        for vid, title, chan, length, views, pub in res[:15]:
            cur = c.execute("INSERT OR IGNORE INTO videos(video_id,url,title,channel,duration,views_text,published_text,query,status,discovered_at) VALUES(?,?,?,?,?,?,?,?, 'discovered', datetime('now'))",
                            (vid, "https://www.youtube.com/watch?v=" + vid, title, chan, length, views, pub, q))
            new += cur.rowcount
        c.commit()
        print(f"{q[:55]:55} -> {len(res)} results")
        time.sleep(2)
    print("new videos:", new, "total:", c.execute("select count(*) from videos").fetchone()[0])
