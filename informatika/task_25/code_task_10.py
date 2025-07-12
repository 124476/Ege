from fnmatch import *

def div(x):
    q = set()
    for i in range(1, int(x ** 0.5) + 1):
        if x % i == 0:
            q |= { i, x // i }
    return sorted(q)

for x in range(0, 10 ** 7 + 1):
    if fnmatch(str(x), "9?*55*7"):
        print(x, sum(div(x)) % 21)