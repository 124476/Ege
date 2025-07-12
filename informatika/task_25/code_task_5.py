def p(x):
    return x > 1 and all(x % i != 0 for i in range(2, int(x ** 0.5) + 1))


def div(x):
    d = set()
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            d |= {i, x // i, }

    return sorted(d)


for i in range(174457, 174505+1):
    d = [ x for x in div(i) if p(x)]

    if sum(d) % 100 == 25:
        print(i, sum(d))