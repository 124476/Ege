from itertools import *

def f(x, y, z, w):
    return ((w <= y) <= x) or not z

table = [(1, 0, 0), (1, 0, 1)]

for p in permutations("xyzw"):
    if [f(**dict(zip(p, row))) for row in table]==[0,1]:
        print(p)