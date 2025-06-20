# Первый вариант
from itertools import *

d = set()

for x in permutations("АССАСИН"):
    m = "".join(x)
    d.add(m)

print(len(d))

# Второй вариант
from itertools import *

sm = 0

for x in set(permutations("АССАСИН")):
    m = "".join(x)
    sm += 1

print(sm)