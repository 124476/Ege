# Первый вариант
sm = 0

for a in "ЛТ":
    for b in "ЛЕТО":
        for c in "ЛЕТО":
            for d in "ЛЕТО":
                m = a + b + c + d
                sm += 1

print(sm)

# Второй вариант
from itertools import *

sm = 0
for x in product("ЛТ", "ЛЕТО", "ЛЕТО", "ЛЕТО"):
    m = "".join(x)
    sm += 1

print(sm)