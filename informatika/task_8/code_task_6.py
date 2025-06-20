from itertools import *

sm = 0

for x in permutations("КАЛИЙ"):
    m = "".join(x)
    if m[0] != "Й" and "ИА" not in m:
        sm += 1

print(sm)