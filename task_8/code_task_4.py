from itertools import *

sm = 0

for x in product("ЛЕТО", repeat=4):
    m = "".join(x)
    if m.count("Е") >= 1:
        sm += 1

print(sm)