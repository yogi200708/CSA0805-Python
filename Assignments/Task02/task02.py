from decimal import Decimal
payments = ["33.40"] * 1000 + ["0.10"] * 3
total_float = 0.0
total_decimal = Decimal("0.00")
for p in payments:
    total_float += float(p)
    total_decimal += Decimal(p)
print("Float total:", total_float)
print("Decimal total:", total_decimal)
print("0.1 + 0.2 == 0.3:", 0.1 + 0.2 == 0.3)
print("Decimal equality:", Decimal("0.1") + Decimal("0.2") == Decimal("0.3"))
# Decimal(float(p)) can preserve the float approximation; use Decimal(p).
