def f(n, x):
    a = []

    while n > 0:
        a += [n % x]
        n //= x

    return a[::-1]


for x in range(0, 1000):
    sm = 81 ** 20 - 9 ** x + 50

    if sum(f(sm, 9)) == 138:
        print(x)
