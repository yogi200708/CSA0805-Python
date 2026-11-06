# Alternative: read the whole file at once (uses more memory).
from decimal import Decimal
with open("mess_oct.txt", encoding="utf-8") as f:
    lines = f.read().splitlines()
total = Decimal("0")
for line in lines:
    parts = line.split(",")
    if len(parts) == 3:
        try:
            total += Decimal(parts[2])
        except Exception:
            pass
print("Whole-file total:", total)
