def f(n):
    m = bin(n)[2:]

    if m.count("1") % 2 == 0:
        m = "10" + (m + "0")[2:]
    else: m = "11" + (m + "1")[2:]

    return int(m, 2)


d = []
for i in range(1, 1000):
    r = f(i)

    if r >= 16:
        d += [i]

print(min(d))
