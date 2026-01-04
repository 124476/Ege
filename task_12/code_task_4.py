mp = {
    "k0": "kR1",

    "11": "kR2",
    "01": "0R3",

    "k2": "kS2",
    "12": "0R3",
    "02": "1R3",

    "k3": "kS3",
    "13": "1R2",
    "03": "0R2",
}


def f(m):
    m = list("k" + m + "k")

    q = 0
    i = 0

    while True:
        c = mp[f"{m[i]}{q}"]

        m[i] = c[0]
        if c[1] == "S": break
        if c[1] == "L": i -= 1
        if c[1] == "R": i += 1

        q = c[2]

    return "".join(m)[1:-1]


print(f(151 * "0").count("1"))