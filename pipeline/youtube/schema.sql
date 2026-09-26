CREATE TABLE IF NOT EXISTS videos (
    video_id        TEXT PRIMARY KEY,
    url             TEXT NOT NULL,
    title           TEXT,
    channel         TEXT,
    duration        TEXT,
    views_text      TEXT,
    published_text  TEXT,
    query           TEXT,            -- search query that first found it
    status          TEXT NOT NULL DEFAULT 'discovered',
                                     -- discovered | transcript_ok | no_transcript | summarized | skipped
    transcript_lang TEXT,
    transcript_auto INTEGER,         -- 1 = auto-generated captions
    transcript_words INTEGER,
    transcript_path TEXT,            -- local cache file, gitignored
    topic           TEXT,            -- filled at summary stage
    relevance       INTEGER,         -- 1-5, filled at summary stage
    speaker_role    TEXT,            -- e.g. former AO, current AO, consultant, student
    summary_path    TEXT,            -- JSON with paraphrased insights
    error           TEXT,
    discovered_at   TEXT,
    transcript_at   TEXT,
    summarized_at   TEXT
);
CREATE INDEX IF NOT EXISTS idx_videos_status ON videos(status);
CREATE INDEX IF NOT EXISTS idx_videos_channel ON videos(channel);
