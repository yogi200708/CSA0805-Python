def read_records(path):
    with open(path, encoding="utf-8") as f:
        return [line.strip().split(",") for line in f if line.strip()]
