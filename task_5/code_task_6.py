def f(n):
    m = bin(n)[2:]

    if len(m) % 2 == 0:
        m = m[:len(m) // 2] + "1" + m[len(m) // 2:]

    return int(m, 2)


for i in range(1, 1000):
    r = f(i)

    if r <= 26:
        print(i)