CREATE TABLE fee_estimates(
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  estimator_id INTEGER NOT NULL,
  timestamp INTEGER NOT NULL,
  target_blocks INTEGER NOT NULL,
  feerate_sat_vb REAL NOT NULL,
  mempool_size_vb INTEGER,
  FOREIGN KEY (estimator_id) REFERENCES estimators(id)
);

CREATE TABLE blocks(
  height INTEGER PRIMARY KEY,
  hash TEXT NOT NULL,
  timestamp INTEGER NOT NULL
);

CREATE TABLE estimators (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    version TEXT,
    source TEXT,
    UNIQUE(name, version)
);