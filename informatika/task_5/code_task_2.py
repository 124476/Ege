def f(n):
    m = bin(n)[2:]

    k = m.count("1")
    m += str(k % 2)

    k = m.count("1")
    m += str(k % 2)

    return int(m, 2)


k = 0
for i in range(1, 1000):
    r = f(i)
    if 210 <= r <= 260:
        k += 1

print(k)
