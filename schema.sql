DROP TABLE IF EXISTS reports;

CREATE TABLE reports (
  scan_id TEXT UNIQUE NOT NULL,
  resource TEXT NOT NULL,
  url TEXT NOT NULL,
  response_code INTEGER NOT NULL,
  scan_date TEXT NOT NULL,
  permalink TEXT NOT NULL,
  verbose_msg TEXT NOT NULL,
  filescan_id TEXT,
  positives TEXT NOT NULL,
  total TEXT NOT NULL
);