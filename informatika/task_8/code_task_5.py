from itertools import *

sm = 0

for x in product("БЕРКЛИЙ", repeat=4):
    m = "".join(x)
    if m[0] != "Й" and ("Е" in m or "И" in m):
        sm += 1

print(sm)
