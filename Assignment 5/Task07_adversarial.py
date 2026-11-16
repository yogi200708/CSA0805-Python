# Task B2: Adversarial data examples
import csv
import io
import sqlite3

def read_csv_text(text):
    try:
        reader = csv.DictReader(io.StringIO(text))
        if not reader.fieldnames or "station" not in reader.fieldnames:
            print("Error: required station column is missing")
            return
        print(list(reader))
    except Exception as e:
        print("CSV error:", e)

print("Missing column:")
read_csv_text("date,pm25\n2026-10-01,48")
print("Wrong delimiter:")
read_csv_text("station;date;pm25\nAdyar;2026-10-01;48")
print("Empty file:")
read_csv_text("")

con = sqlite3.connect(":memory:")
con.execute("CREATE TABLE aq(station TEXT, pm25 REAL)")
con.execute("INSERT INTO aq VALUES (?, ?)", ("Adyar", 48))

name = "Adyar' OR '1'='1"
safe = con.execute("SELECT AVG(pm25) FROM aq WHERE station=?", (name,)).fetchone()[0]
print("Parameterized query result:", safe)
con.close()
