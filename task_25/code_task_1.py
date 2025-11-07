def div(x):
    d = set()
    for i in range(1, int(x ** 0.5) + 1):
        if x % i == 0:
            d |= {i, x // i}
    return sorted(d)


for i in range(193136, 193223 + 1):
    d = div(i)

    if len(d) == 6:
        print(*d)
