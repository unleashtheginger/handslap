DROP TABLE IF EXISTS hits;

CREATE TABLE sites (
id INTEGER PRIMARY KEY AUTOINCREMENT,
url_root TEXT UNIQUE NOT NULL,
hits INTEGER NOT NULL
);
