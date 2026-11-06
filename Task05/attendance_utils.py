def read_records(path):
    with open(path, encoding="utf-8") as f:
        return [line.strip().split(",") for line in f if line.strip()]
def percentage(present, total):
    return present / total * 100 if total else 0
