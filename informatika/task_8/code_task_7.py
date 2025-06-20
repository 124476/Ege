from itertools import *

sm = 0

for x in permutations("КОЛУН"):
    m = "".join(x)

    m = m.replace("Л", "К").replace("Н", "К")

    m = m.replace("У", "О")

    if "КК" not in m and "ОО" not in m:
        sm += 1

print(sm)