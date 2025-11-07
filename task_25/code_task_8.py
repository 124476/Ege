from fnmatch import *

def div(x):
    q = set()

    for i in range(1, int(x ** 0.5) + 1):
        if x % i == 0:
            q |= { i, x // i }

    return sorted(q)

for x in range(0, 10 ** 7, 6 * 7 * 4):
    if fnmatch(str(x), "?8*8*?8"):
        print(x, sum(div(x)))