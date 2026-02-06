import sqlite3
from pathlib import Path


def init_db(db_path="fee_benchmark.db"):
    connection = sqlite3.connect(db_path)
    with open("storage/schema.sql") as f:
        connection.executescript(f.read())
    connection.commit()
    return connection