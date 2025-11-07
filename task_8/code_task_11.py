from itertools import *

k = 0

for x in sorted(product("АКРУ", repeat=5)):
    m = "".join(x)
    k += 1

    # print(k, m)

    if k == 150:
        print(m)
