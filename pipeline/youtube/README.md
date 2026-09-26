# YouTube video tracking database

Tracks every college-counseling video found, what state it is in, and where its summary lives.

**Database:** `youtube_videos.db` (SQLite), one table `videos` (schema in `schema.sql`).

| Status | Meaning |
|:--|:--|
| `discovered` | Found by a search query; no transcript yet |
| `transcript_ok` | Transcript downloaded to `transcripts/<video_id>.txt` |
| `no_transcript` | Captions unavailable or disabled (reason in `error`) |
| `summarized` | Paraphrased summary written to `summaries/<video_id>.json` |

Other columns: `title`, `channel`, `duration`, `views_text`, `published_text`, `query` (first query that found it), `transcript_lang`, `transcript_auto` (1 = auto captions), `transcript_words`, `topic`, `relevance` (1-5), `speaker_role`, and timestamps.

**Scripts (run from this folder, in order):**
1. `python discover.py` - searches YouTube for the queries in the script, adds new videos as `discovered` (safe to re-run; existing rows are kept).
2. `python fetch_transcripts.py [N]` - downloads transcripts for `discovered` videos. YouTube rate-limits after about 30 requests; the script stops without changing status when it is blocked. Re-run later and it resumes.
3. Summarize (agents write `summaries/<video_id>.json`), then `python ingest_summaries.py` to update the database.

**Useful queries:**
```sql
select status, count(*) from videos group by 1;
select video_id, title, channel, relevance from videos where status='summarized' order by relevance desc;
select video_id, title from videos where status='discovered' limit 20;
```

`transcripts/` is gitignored (copyrighted text kept local only). `summaries/`, the database and the scripts can be committed. Output file: `qualitative_insights/YouTube College Counseling Video Insights.md`.
