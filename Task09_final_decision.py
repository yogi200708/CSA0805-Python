# Task B4: Index and simple sentiment agreement
import sqlite3
import time

con = sqlite3.connect(":memory:")
con.execute("CREATE TABLE readings(station TEXT, day TEXT, pm25 REAL)")
rows = [(f"Station{i%10}", f"2026-10-{i%30+1:02d}", float(i%150)) for i in range(50000)]
con.executemany("INSERT INTO readings VALUES (?, ?, ?)", rows)
con.commit()

start = time.perf_counter()
con.execute("SELECT AVG(pm25) FROM readings WHERE station=? AND day=?",
            ("Station1", "2026-10-01")).fetchone()
print("Query time before index:", round(time.perf_counter()-start, 6))

con.execute("CREATE INDEX idx_station_day ON readings(station, day)")
start = time.perf_counter()
con.execute("SELECT AVG(pm25) FROM readings WHERE station=? AND day=?",
            ("Station1", "2026-10-01")).fetchone()
print("Query time after index:", round(time.perf_counter()-start, 6))

con.close()
