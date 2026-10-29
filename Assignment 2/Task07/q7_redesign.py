# TASK 7: Diagnose, redesign and validate
# Chosen redesign: replace repeated staircase recursion with memoization.
from functools import lru_cache
from time import perf_counter
naive_calls = 0
def ways_naive(n):
    global naive_calls
    naive_calls += 1
    if n <= 1: return 1
    return ways_naive(n-1) + ways_naive(n-2)

memo_calls = 0
@lru_cache(maxsize=None)
def ways_memo(n):
    global memo_calls
    memo_calls += 1
    if n <= 1: return 1
    return ways_memo(n-1) + ways_memo(n-2)

n = 25
start = perf_counter(); original = ways_naive(n); t1 = perf_counter() - start
start = perf_counter(); improved = ways_memo(n); t2 = perf_counter() - start
print("Input:", n)
print("Original result/calls/time:", original, naive_calls, f"{t1:.6f}s")
print("Improved result/calls/time:", improved, memo_calls, f"{t2:.6f}s")
print("Same answer:", original == improved)
print("Memoization reduces repeated calculations but uses extra cache memory.")
print("Record your own timing results; times depend on your computer.")
