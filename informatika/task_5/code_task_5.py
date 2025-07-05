def f(n):
    m = bin(n)[2:].zfill(8)

    m = m.replace("0", "p")
    m = m.replace("1", "0")
    m = m.replace("p", "1")

    return int(m, 2) + 1

for i in range(1, 128):
    r = f(i)

    if r == 153:
        print(i)
