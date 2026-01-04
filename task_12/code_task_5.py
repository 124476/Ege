mp = {
    "k0": "kL1",

    "k1": "kS1",
    "11": "0L3",
    "01": "1L2",

    "k2": "kS2",
    "12": "0L1",
    "02": "0L3",

    "k3": "kS3",
    "13": "1L2",
    "03": "1L1",
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


print(f(45 * "0" + 21 * "1").count("0"))