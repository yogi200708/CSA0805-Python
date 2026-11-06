from pathlib import Path
def read_files(folder, error_log):
    records = []
    errors = []
    for path in sorted(Path(folder).glob("*.txt")):
        try:
            with path.open(encoding="utf-8") as f:
                for line_no, line in enumerate(f, start=1):
                    records.append((path.name, line_no, line.strip()))
        except (FileNotFoundError, PermissionError, UnicodeDecodeError) as e:
            errors.append(f"{path.name},0,{type(e).__name__},{e}")
    return records, errors
