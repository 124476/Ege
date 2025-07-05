def f(n, m):
    p1 = 1
    for p in [x for x in str(n) if int(x) % 2 == 1 and x != "0"] + [x for x in str(m) if int(x) % 2 == 1 and x != "0"]:
        p1 *= int(p)

    p2 = 1
    for p in [x for x in str(n) if int(x) % 2 == 0 and x != "0"] + [x for x in str(m) if int(x) % 2 == 0 and x != "0"]:
        p2 *= int(p)

    return abs(p1 - p2)


for i in range(1, 10000):
    r = f(120, i)

    if r == 29:
        print(i)