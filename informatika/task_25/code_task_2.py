def div(x):
    d = set()
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            d |= { i, x // i, }

    return sorted(d)

for i in range(1_500_001, 1_500_100):
    d = div(i)
    if len(d) == 0: f = 0
    else: f = sum(d) // len(d)

    if str(f)[-1] == "9":
        print(i, f)