def f(n):
    m = bin(n)[2:]
    if m.count("1") % 2 == 0: m += "0"
    else: m += "1"

    if m.count("1") % 2 == 0: m += "0"
    else: m += "1"

    return int(m, 2)


d = []
for i in range(1, 100):
    r = f(i)

    if r > 130:
        d += [r]

print(min(d))