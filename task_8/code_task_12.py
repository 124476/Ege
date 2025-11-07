from itertools import *

k = 0

p = 0

for x in sorted(product("МАНГУСТ", repeat=6)):
    m = "".join(x)
    k += 1

    if m[0] != "У" and m.count("М") == 2 and m.count("Г") <= 1:
        p = k

print(p)