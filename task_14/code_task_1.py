def f(n, x):
    a = []

    while n > 0:
        a += [n % x]
        n //= x

    return a[::-1]


sm = 7 ** 103 + 20 * 7 ** 204 - 3 * 7 ** 57 + 97
print(f(sm, 7).count(6))