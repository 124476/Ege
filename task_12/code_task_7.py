mp = {
    "k0": "kL1",

    "k1": "kS1",
    "01": "1L1",
    "11": "0L1",
}


def f(m):
    m = list("k" + m + "k")

    q = 0
    i = len(m) - 1

    while True:
        c = mp[f"{m[i]}{q}"]

        m[i] = c[0]
        if c[1] == "S": break
        if c[1] == "L": i -= 1
        if c[1] == "R": i += 1

        q = c[2]

    return "".join(m)[1:-1]


for i in range(10000):
    if int(f(bin(i)[2:]), 2) == 156:
        print(i)
