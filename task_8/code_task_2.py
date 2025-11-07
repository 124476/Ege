from itertools import *

sm = 0

for x in product("КРОТ", repeat = 6): # repeat - повтор 6 раз
    m = "".join(x)

    if m.count("О") == 1:
        sm += 1

print(sm)