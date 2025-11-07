from itertools import *

sm = 0

for x in product("01", repeat=11):
    m = "".join(x)

    if m.count("1") == 4 and "11" not in m:
        if m[0] == "0": sm += 3 * 4 ** 10
        else: sm += 4 ** 11

print(sm)
