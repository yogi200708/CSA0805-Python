def write_report(rows, path):
    with open(path, "w", encoding="utf-8") as f:
        for row in rows:
            f.write(",".join(row) + "\\n")
