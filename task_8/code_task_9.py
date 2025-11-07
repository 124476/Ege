from itertools import *

sm = 0

for x in permutations("12345670", 6):
    m = "".join(x)

    if m[0] == "0":
        continue

    m = m.replace("3", "1").replace("5", "1").replace("7", "1")
    m = m.replace("2", "0").replace("4", "0").replace("6", "0")

    if "00" not in m and "11" not in m:
        sm += 1

print(sm)
