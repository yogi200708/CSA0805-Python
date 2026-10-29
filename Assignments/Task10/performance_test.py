from decimal import Decimal
from time import perf_counter
payments = ["33.40"] * 1000 + ["0.10"] * 3
start = perf_counter()
f = 0.0
for p in payments:
    f += float(p)
float_time = perf_counter() - start
start = perf_counter()
d = Decimal("0.00")
for p in payments:
    d += Decimal(p)
decimal_time = perf_counter() - start
print("Float total:", f)
print("Decimal total:", d)
print("Float seconds:", float_time)
print("Decimal seconds:", decimal_time)
for size in [300, 6000, 150000]:
    data = ["0.10"] * size
    start = perf_counter()
    total = 0.0
    for x in data:
        total += float(x)
    print(size, "float seconds:", perf_counter() - start)
    start = perf_counter()
    total_d = Decimal("0.00")
    for x in data:
        total_d += Decimal(x)
    print(size, "Decimal seconds:", perf_counter() - start)
