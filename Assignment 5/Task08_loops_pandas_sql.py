# Task B3: Compare Python loop, pandas and SQL (small dataset)
import csv
import io
import sqlite3
from collections import defaultdict

raw = """station,date,pm25
Adyar,2026-10-01,48
Adyar,2026-10-01,52
Guindy,2026-10-01,95
Guindy,2026-10-02,121
"""

# Python loop
groups = defaultdict(list)
for row in csv.DictReader(io.StringIO(raw)):
    groups[(row["station"], row["date"])].append(float(row["pm25"]))
print("Python loop:")
for key, vals in groups.items():
    print(key, round(sum(vals)/len(vals), 2))

# Pandas groupby
try:
    import pandas as pd
    df = pd.read_csv(io.StringIO(raw))
    print("\nPandas groupby:")
    print(df.groupby(["station", "date"])["pm25"].mean())
except ImportError:
    print("\nInstall pandas: pip install pandas")

# SQL GROUP BY
con = sqlite3.connect(":memory:")
con.execute("CREATE TABLE aq(station TEXT, day TEXT, pm25 REAL)")
con.executemany("INSERT INTO aq VALUES (?, ?, ?)", [
    (r["station"], r["date"], float(r["pm25"]))
    for r in csv.DictReader(io.StringIO(raw))
])
print("\nSQL GROUP BY:")
for row in con.execute("SELECT station, day, AVG(pm25) FROM aq GROUP BY station, day"):
    print(row)
con.close()
