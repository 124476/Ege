from itertools import *

def f(x, y, w, z):
    return ((y <= x) or (not z and w)) == (w == x)

for a in product([0, 1], repeat=3):
    table = [(a[0], 1, 0, 0), (0, 0, 0, 1), (0, 1, a[1], a[2])]

    if len(table) != len(set(table)):
        continue

    for p in permutations("xywz"):
        if [f(**dict(zip(p, row))) for row in table] == [1, 1, 1]:
            print(p)