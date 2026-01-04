mp = {
    "k0": "kL1",

    "01": "2L1",
    "11": "0R2",
    "21": "1L1",

    "k2": "kS2",
    "12": "0R2",
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


print(f(106 * "0" + 334 * "1" + 560 * "2").count("0"))
