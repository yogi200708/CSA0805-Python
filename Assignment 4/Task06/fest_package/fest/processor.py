from collections import defaultdict
from .reader import read_files
from .validator import parse_record
from .report import write_outputs

def run(input_folder="input", output_folder="output"):
    raw, errors = read_files(input_folder, "errors.log")
    students = {}
    seen = set()
    event_members = defaultdict(set)
    for filename, line_no, line in raw:
        try:
            item = parse_record(line)
            if item["reg"] in seen:
                # Duplicate registration: combine events, retain first student details.
                students[item["reg"]]["events"].update(item["events"])
            else:
                seen.add(item["reg"])
                item["events"] = set(item["events"])
                students[item["reg"]] = item
            for event in item["events"]:
                event_members[event].add(item["reg"])
        except ValueError as e:
            errors.append(f"{filename},{line_no},{type(e).__name__},{e},{line}")
    write_outputs(students, event_members, errors, output_folder)
    return students, event_members, errors
