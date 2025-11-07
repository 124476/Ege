def cc(x, p):
    a = ""
    q = "0123456789" + "".join([chr(i) for i in range(ord("a"), ord("z") + 1)])

    while x > 0:
        a = q[x % p] + a
        x //= p

    return a

def f(n):
    m = cc(n, 3)

    if n % 3 == 0:
        m = "1" + m + "02"
    else: m += cc((n % 3) * 4, 3)

    return int(m, 3)

d = []
for i in range(1, 1000):
    r = f(i)

    if r < 199:
        d += [i]

print(max(d))
