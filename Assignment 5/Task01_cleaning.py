# Task B1: Simple data cleaning
import csv
import io

raw = """station,date,pm25
Adyar,2026-10-01,48
Adyar,2026-10-02,NA
Adyar,2026-10-03,
Guindy,2026-10-01,95
Guindy,2026-10-02,-5
Guindy,2026-10-03,121
Guindy,2026-10-04,1200
"""

print("BEFORE CLEANING:")
print(raw)

rows = []
reader = csv.DictReader(io.StringIO(raw))
for row in reader:
    value = row["pm25"].strip()
    if value == "" or value.upper() == "NA":
        continue
    pm25 = float(value)
    if pm25 < 0 or pm25 > 999:
        continue
    rows.append((row["station"], row["date"], pm25))

print("AFTER CLEANING:")
print(rows)
