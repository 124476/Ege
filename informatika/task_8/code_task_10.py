from itertools import *

sm = 0

for x in product("12345670", repeat=4):
    m = "".join(x)

    if m[0] in "246" and m[0] >= m[1] >= m[2] >= m[3]:
        sm += 1

print(sm)
