from functools import *


@lru_cache(None)
def f(n):
    if n < 4: return 1
    if n > 3 and n % 2 == 1: return n
    return f(n - 1) + f(n - 2) + f(n - 3)


for i in range(1, 3000):
    f(i)

print(f(2254) - f(2252))