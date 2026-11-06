import re
def parse_record(line):
    fields = line.split(",")
    if len(fields) != 5:
        raise ValueError(f"expected 5 fields, found {len(fields)}")
    reg, name, dept, email, events = [x.strip() for x in fields]
    if not reg or not name or not dept:
        raise ValueError("register/name/department missing")
    if "@" not in email or email.startswith("@") or email.endswith("@") or "." not in email.split("@")[-1]:
        raise ValueError(f"invalid email {email!r}")
    chosen = [e.strip() for e in events.split(";") if e.strip()]
    if not chosen:
        raise ValueError("no events selected")
    return {"reg":reg, "name":name, "dept":dept, "email":email, "events":chosen}
