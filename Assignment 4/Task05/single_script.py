# Organisation A: everything in one script
def read_records(path):
    with open(path, encoding="utf-8") as f:
        return [line.strip().split(",") for line in f if line.strip()]
def percentage(present, total):
    return present / total * 100 if total else 0
def write_report(rows, path):
    with open(path, "w", encoding="utf-8") as f:
        for row in rows: f.write(",".join(row) + "\\n")
if __name__ == "__main__":
    print("Single-script version ready.")
