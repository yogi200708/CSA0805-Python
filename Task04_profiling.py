# Task A4/B3: Basic timing and profiling
import time
import cProfile

def work():
    total = 0
    for i in range(100000):
        total += i
    return total

start = time.perf_counter()
print("Result:", work())
print("Time:", round(time.perf_counter() - start, 6), "seconds")

print("\n cProfile output:")
cProfile.run("work()")
