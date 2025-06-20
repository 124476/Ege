from itertools import *

sm = 0

for x in product("ТИМАШЕВСК", repeat=5):
    m = "".join(x)

    for i in "ИАЕ": m = m.replace(i, "1")

    if "Ш1" not in m and "1Ш" not in m:
        for i in "ТМШВСК": m = m.replace(i, "0")

        if m.count("1") > m.count("0"):
            sm += 1

print(sm)