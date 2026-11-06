from pathlib import Path
def write_outputs(students, event_members, errors, folder):
    out = Path(folder); out.mkdir(parents=True, exist_ok=True)
    with (out/"master.csv").open("w", encoding="utf-8") as f:
        f.write("Register,Name,Department,Email,Events\\n")
        for reg, s in sorted(students.items()):
            f.write(f"{reg},{s['name']},{s['dept']},{s['email']},{';'.join(sorted(s['events']))}\\n")
    for event, regs in event_members.items():
        safe = "".join(c if c.isalnum() else "_" for c in event)
        with (out/f"{safe}_participants.txt").open("w", encoding="utf-8") as f:
            for reg in sorted(regs): f.write(reg+"\\n")
    with (out/"summary.txt").open("w", encoding="utf-8") as f:
        f.write(f"Unique registrations: {len(students)}\\n")
        f.write(f"Events: {len(event_members)}\\n")
        for event, regs in sorted(event_members.items()):
            f.write(f"{event}: {len(regs)} participants\\n")
    with (out/"error_log.csv").open("w", encoding="utf-8") as f:
        f.write("File,Line,Error,Message,Content\\n")
        f.write("\\n".join(errors))
