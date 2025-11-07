from itertools import *

a = '24 146 45 12356 34 24'.split()
s = 'CD DE DB CB BE BG BA AG'.split()
print(*range(1, 7))

for p in permutations('ABCDEG'):
    if all(str(p.index(x) + 1) in a[p.index(y)] for x, y in s):
        print(*p)
        break
