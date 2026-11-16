# TASK 3: Vehicle Registration Number Validator (no regular expressions)
def normalise(text):
    return text.strip().upper().replace(" ", "").replace("-", "")

def is_valid(reg):
    if len(reg) not in (9, 10): return False
    if not reg[0:2].isalpha() or not reg[2:4].isdigit(): return False
    if len(reg) == 9:
        series, digits = reg[4:5], reg[5:9]
    else:
        series, digits = reg[4:6], reg[6:10]
    return series.isalpha() and digits.isdigit()

def format_number(reg):
    if not is_valid(reg): return "INVALID"
    if len(reg) == 9: return reg[:2] + " " + reg[2:4] + " " + reg[4:5] + " " + reg[5:9]
    return reg[:2] + " " + reg[2:4] + " " + reg[4:6] + " " + reg[6:10]

samples = ["tn 09 ab 1234", "KA-01-M-0007", "TN9AB1234", "TN 22 1234 AB",
           "MH 12 DE 1234", "XX-99-ZZ-9999"]
for raw in samples:
    reg = normalise(raw)
    print(f"{raw:16} -> {reg:10} {'valid' if is_valid(reg) else 'INVALID'}")
    if is_valid(reg): print(" Receipt:", format_number(reg))
print("Strings are immutable: upper() returns a new string instead of changing the original.")
