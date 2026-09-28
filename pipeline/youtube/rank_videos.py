# Scores videos with status='discovered' so the most informative ones are downloaded first.
# Heuristics only (title, channel, duration, views); re-run any time. Writes videos.priority.
import os, re, math, sqlite3, collections

HERE = os.path.dirname(os.path.abspath(__file__))
c = sqlite3.connect(os.path.join(HERE, "youtube_videos.db"))
cols = [r[1] for r in c.execute("pragma table_info(videos)")]
if "priority" not in cols:
    c.execute("alter table videos add column priority REAL")

def secs(d):
    if not d:
        return None
    try:
        p = [int(x) for x in d.split(":")]
    except ValueError:
        return None
    t = 0
    for x in p:
        t = t * 60 + x
    return t

def views(v):
    if not v or "No views" in v:
        return 0
    m = re.search(r"([\d,]+)", v)
    return int(m.group(1).replace(",", "")) if m else 0

def has(t, pats):
    return any(re.search(p, t) for p in pats)

OFFICIAL_CH = re.compile(r"(harvard|yale|stanford|princeton|columbia|cornell|dartmouth|\bbrown\b|penn |upenn|\bmit\b|duke|northwestern|johns hopkins|vanderbilt|georgia tech|caltech|rice |emory|georgetown|\buniversity\b|\bcollege admission|undergraduate admission|admissions office|office of admission|admission office)", re.I)
GOOD_CH = {"college essay guy": 2.5, "ask dr. hoffman": 1.0, "your college-bound kid": 2.5, "the college talk show": 1.0,
           "admittedly: college admissions with thomas caleel": 1.0, "collegeadvisor": 1.5, "ingenius prep": 1.0,
           "college admissions insider": 1.0, "collegevine": 1.0, "college admissions counselors - egelloc": 0.0}
PROMO_CH = {"elevated school": -1.5, "shinwoo lee": -2.0, "pratik vangal": -1.0, "crimson education": -1.0, "supertutortv": -1.0}

rows = c.execute("select video_id,title,channel,duration,views_text from videos where status='discovered'").fetchall()
scored = []
for vid, title, ch, dur, vw in rows:
    t = (title or "").lower()
    chl = (ch or "").lower()
    s = 0.0
    d = secs(dur)
    if d is None:
        s -= 1
    elif d < 180: s -= 4
    elif d < 480: s += 1
    elif d <= 3600: s += 3
    elif d <= 5700: s += 1.5
    else: s -= 1
    v = views(vw)
    s += min(2.0, math.log10(v + 1) / 2.5)
    if v == 0: s -= 1
    if OFFICIAL_CH.search(ch or ""): s += 2.5
    s += GOOD_CH.get(chl, 0) + PROMO_CH.get(chl, 0)
    if has(t, [r"admissions? officer", r"admission officer", r"dean of admission", r"former ao", r"admissions? (director|counselor|dean)", r"admission counsel"]): s += 2.5
    if has(t, [r"committee", r"how .{0,25}(read|review|evaluat|decid)", r"inside", r"behind the scenes", r"mock", r"walkthrough", r"real application", r"my .{0,20}(file|application)"]): s += 2
    # under-covered topics get a boost
    if has(t, [r"financial aid", r"\bfafsa\b", r"\bcss\b", r"scholarship", r"merit", r"award letter", r"aid appeal", r"afford", r"net price", r"cost of"]): s += 2.5
    if has(t, [r"computer science", r"\bcs\b", r"\bstem\b", r"engineering", r"coding", r"robotics", r"research (program|opportunit)", r"summer program"]): s += 2.5
    if has(t, [r"early decision", r"early action", r"\bed\b", r"\bea\b", r"waitlist", r"defer"]): s += 2
    if has(t, [r"test.optional", r"\bsat\b", r"\bact\b", r"standardized"]): s += 1.5
    if has(t, [r"extracurricular", r"activit", r"honors", r"awards"]): s += 1.5
    if has(t, [r"recommendation", r"letters? of rec"]): s += 1.5
    if has(t, [r"interview"]): s += 1.5
    if has(t, [r"freshman", r"9th grade", r"course (planning|selection)", r"high school (plan|course)", r"\bap\b", r"rigor", r"gpa"]): s += 2
    if has(t, [r"first.gen", r"international", r"demonstrated interest", r"holistic", r"myth", r"trend"]): s += 1.5
    if has(t, [r"reach.{0,10}target", r"college list", r"list of (schools|colleges)"]): s += 0.5
    if not has(t, [r"admission", r"college", r"universit", r"appl(y|ic)", r"financial aid", r"fafsa", r"scholarship", r"sat", r"act", r"counsel", r"gpa", r"school"]): s -= 5
    if "business" in chl: s -= 5
    # saturated / promo / off-topic
    if has(t, [r"essay", r"personal statement", r"supplement", r"\bpiq\b", r"why us", r"common app (prompt|essay)"]): s -= 3
    if has(t, [r"in \d+ minutes?", r"3x", r"secret", r"hack", r"shocking", r"trick"]): s -= 1
    if has(t, [r"law school", r"\blsat\b", r"\bmba\b", r"medical school", r"\bmcat\b", r"\bphd\b", r"graduate school", r"grad school", r"\bmbbs\b", r"cutoff", r"\bneet\b", r"\bjee\b", r"\bucas\b", r"oxford", r"cambridge", r"downing", r"tuck", r"residency"]): s -= 8
    if has(t, [r"nursing", r"pre.?med"]): s -= 2
    scored.append([vid, s, title, ch, dur, v])

# diminishing returns per channel so one channel doesn't fill the queue
scored.sort(key=lambda r: -r[1])
seen = collections.Counter()
final = []
for r in scored:
    adj = r[1] - 0.6 * seen[r[3]]
    seen[r[3]] += 1
    final.append((adj, r))
final.sort(key=lambda x: -x[0])
for adj, r in final:
    c.execute("update videos set priority=? where video_id=?", (round(adj, 2), r[0]))
c.commit()
print("ranked", len(final))
if __name__ == "__main__":
    import sys
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 40
    for adj, r in final[:n]:
        print(f"{adj:5.1f} | {str(r[4]):8} | {str(r[3])[:22]:22} | {str(r[2])[:80]}")
    print("...")
    for adj, r in final[-8:]:
        print(f"{adj:5.1f} | {str(r[4]):8} | {str(r[3])[:22]:22} | {str(r[2])[:80]}")
