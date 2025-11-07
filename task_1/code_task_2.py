from itertools import *

s1 = "1457 2358 32458 41367 5123 6478 7146 8236"
s2 = "АБГЕ БАДВ ВБДИ ГАЕЖД ДГБВИ ЕАГЖ ЖЕГИ ИЖДВ"

s2 = { i[0]: frozenset(i[1:]) for i in s2.split() }

print("1 2 3 4 5 6 7 8")
for p in permutations("АБВГДЕЖИ"):
    s3 = s1
    for x, y in zip("12345678", p):
        s3 = s3.replace(x, y)

    s3 = { i[0]: frozenset(i[1:]) for i in s3.split() }

    if s2 == s3:
        print(*p)