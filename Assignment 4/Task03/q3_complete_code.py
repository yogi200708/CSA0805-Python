import os
import tempfile

class InvalidRecord(Exception):
    """Raised when an attendance line has an invalid format."""

def parse_line(line):
    parts = line.strip().split(",")
    if len(parts) != 3:
        raise InvalidRecord(f"expected 3 fields, found {len(parts)}")
    if parts[2] not in ("P", "A"):
        raise InvalidRecord(f"invalid status {parts[2]!r}")
    return tuple(parts)

def summarise(path):
    present, absent, errors = 0, 0, []
    try:
        with open(path, encoding="utf-8") as file:
            for line_no, line in enumerate(file, start=1):
                try:
                    reg, date, status = parse_line(line)
                except InvalidRecord as error:
                    errors.append((line_no, str(error)))
                else:
                    if status == "P":
                        present += 1
                    else:
                        absent += 1
    except FileNotFoundError as error:
        raise FileNotFoundError(f"Attendance file not found: {path}") from error
    finally:
        print("File processing finished.")
    return present, absent, errors

if __name__ == "__main__":
    data = ("192311001,2026-10-08,P\\n192311002,2026-10-08,A\\n"
            "192311003,2026-10-08\\n192311004,2026-10-08,L\\n")
    with tempfile.NamedTemporaryFile("w", suffix=".csv", delete=False,
                                     encoding="utf-8") as tmp:
        tmp.write(data)
        name = tmp.name
    print(summarise(name))
    os.remove(name)
    try:
        summarise("missing_attendance.csv")
    except FileNotFoundError as error:
        print(error)
