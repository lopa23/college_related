# Reads summaries/<video_id>.json written by summarizer agents and updates the tracking DB.
import os, json, sqlite3, glob

HERE = os.path.dirname(os.path.abspath(__file__))
c = sqlite3.connect(os.path.join(HERE, "youtube_videos.db"))
n = 0
for p in glob.glob(os.path.join(HERE, "summaries", "*.json")):
    vid = os.path.splitext(os.path.basename(p))[0]
    try:
        s = json.load(open(p, encoding="utf8"))
    except Exception as e:
        print("bad json", p, e); continue
    c.execute("update videos set status='summarized', topic=?, relevance=?, speaker_role=?, summary_path=?, summarized_at=datetime('now') where video_id=?",
              (s.get("topic"), s.get("relevance"), s.get("speaker_role"), p, vid))
    n += c.total_changes and 1
c.commit()
print("ingested", n)
for r in c.execute("select status,count(*) from videos group by 1"): print(r)
