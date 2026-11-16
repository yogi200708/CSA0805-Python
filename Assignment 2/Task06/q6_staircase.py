# TASK 6: Staircase ways - recursion, memoization and loop
from functools import lru_cache
import sys
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

def ways_loop(n):
    a = b = 1
    if n <= 1: return 1
    for _ in range(2, n+1):
        a, b = b, a+b
    return b

for n in range(1, 7): print("n =", n, "ways =", ways_loop(n))
naive_calls = 0
print("Naive n=25:", ways_naive(25), "calls:", naive_calls)
ways_memo.cache_clear()
memo_calls = 0
print("Memo n=25:", ways_memo(25), "calls:", memo_calls)
print("Loop n=1000 result has", len(str(ways_loop(1000))), "digits.")
print("Recursion limit:", sys.getrecursionlimit(), "- the loop avoids stack depth limits.")
