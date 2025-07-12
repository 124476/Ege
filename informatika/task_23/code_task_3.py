from functools import *


@lru_cache(None)
def f(c, e, d):
    if c > e: return 0
    if c == e: return 12 in d
    return f(c + 1, e, d + (c,)) + f(c * 2, e, d + (c,))

print(f(1, 30, (1,)))