# Fetches transcripts for videos with status='discovered' and caches them locally (gitignored).
# Usage: python fetch_transcripts.py [max_videos]
import os, sys, time, sqlite3
from youtube_transcript_api import YouTubeTranscriptApi

HERE = os.path.dirname(os.path.abspath(__file__))
DB = os.path.join(HERE, "youtube_videos.db")
OUT = os.path.join(HERE, "transcripts")
os.makedirs(OUT, exist_ok=True)

limit = int(sys.argv[1]) if len(sys.argv) > 1 else 10**9
c = sqlite3.connect(DB)
rows = c.execute("select video_id from videos where status='discovered' limit ?", (limit,)).fetchall()
api = YouTubeTranscriptApi()
ok = fail = 0
blocked = 0
for (vid,) in rows:
    try:
        tlist = api.list(vid)
        try:
            t = tlist.find_transcript(["en", "en-US", "en-GB"])
        except Exception:
            t = next(iter(tlist))
        fetched = t.fetch()
        text = "\n".join(s.text.replace("\n", " ") for s in fetched)
        path = os.path.join(OUT, vid + ".txt")
        open(path, "w", encoding="utf8").write(text)
        c.execute("update videos set status='transcript_ok', transcript_lang=?, transcript_auto=?, transcript_words=?, transcript_path=?, transcript_at=datetime('now'), error=NULL where video_id=?",
                  (t.language_code, 1 if t.is_generated else 0, len(text.split()), path, vid))
        ok += 1
    except Exception as e:
        msg = type(e).__name__ + ": " + str(e).split("\n")[0][:120]
        if "IpBlocked" in msg or "RequestBlocked" in msg or "429" in msg:
            print("YouTube is rate-limiting this IP; stopping without changing status. Re-run later (resumable).")
            break
        c.execute("update videos set status='no_transcript', error=?, transcript_at=datetime('now') where video_id=?", (msg, vid))
        fail += 1
    c.commit()
    if (ok + fail) % 25 == 0:
        print(f"progress ok={ok} fail={fail}")
    time.sleep(4 + (hash(vid) % 30) / 10)
c.commit()
print("done ok=%d fail=%d" % (ok, fail))
