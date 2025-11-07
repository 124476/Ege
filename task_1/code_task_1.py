from itertools import *

s1 = '1248 2157 3456 4136 523 634 728 817'
s2 = 'AFBE BAHE CFGH DGH EAB FAC GCD HCDB'

s2 = { i[0]: frozenset(i[1:]) for i in s2.split() }

print("1 2 3 4 5 6 7 8")
for p in permutations('ABCDEFGH'):
    s3 = s1
    for x, y in zip("12345678", p):
        s3 = s3.replace(x, y)
    s3 = { i[0]: frozenset(i[1:]) for i in s3.split() }

    if s2 == s3:
        print(*p)
