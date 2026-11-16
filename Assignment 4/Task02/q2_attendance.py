from pathlib import Path
from collections import defaultdict

def process_month(folder):
    folder = Path(folder)
    counts = defaultdict(lambda: [0, 0]) # register: [present, total]
    damaged = []

    for path in sorted(folder.glob("*.txt")):
        try:
            with path.open(encoding="utf-8") as f:
                for line_no, line in enumerate(f, start=1):
                    fields = line.strip().split(",")
                    if len(fields) != 3 or fields[2] not in ("P", "A"):
                        damaged.append(f"{path.name},{line_no},{line.strip()}")
                        continue
                    reg, date, status = fields
                    counts[reg][1] += 1
                    if status == "P":
                        counts[reg][0] += 1
        except (FileNotFoundError, PermissionError, UnicodeDecodeError) as e:
            damaged.append(f"{path.name},0,{e}")

    with open("attendance_report.csv", "w", encoding="utf-8") as out:
        out.write("Register,Present,Total,Percentage\\n")
        for reg, (present, total) in sorted(counts.items()):
            pct = present / total * 100 if total else 0
            out.write(f"{reg},{present},{total},{pct:.2f}\\n")

    with open("below_75.txt", "w", encoding="utf-8") as out:
        for reg, (present, total) in sorted(counts.items()):
            pct = present / total * 100 if total else 0
            if pct < 75:
                out.write(f"{reg} - {pct:.2f}%\\n")

    with open("damaged_lines.csv", "w", encoding="utf-8") as out:
        out.write("File,Line,Content_or_Error\\n")
        out.write("\\n".join(damaged))
    print("Attendance reports created.")
    return counts, damaged

if __name__ == "__main__":
    process_month("daily_files")
