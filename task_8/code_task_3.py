from itertools import *

sm = 0

for i in range(4, 7):
    for x in product("АНИМЕ", repeat = i):
        sm += 1

print(sm)