# TASK 4: Build SMS statement and compare string methods
import time
def build_plus(parts):
    text = ""
    for p in parts: text += p + ";"
    return text
def build_join(parts):
    return ";".join(parts) + ";"
def build_fstring(parts):
    return "".join([f"{p};" for p in parts])
def measure(func, parts):
    start = time.perf_counter()
    result = func(parts)
    return result, time.perf_counter() - start

for size in [1000, 10000, 200000]:
    items = [f"Item{i}:Rs{i % 50}" for i in range(size)]
    a, ta = measure(build_plus, items)
    b, tb = measure(build_join, items)
    c, tc = measure(build_fstring, items)
    print("Items:", size, "| same output:", a == b == c, "| length:", len(a))
    print(f"+= {ta:.4f}s | join {tb:.4f}s | f-string {tc:.4f}s")
print("Run three times and calculate average times. Times vary by computer.")
