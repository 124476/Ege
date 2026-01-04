mp = {
    "k0": "kL1",
    "k2": "kS2",
    "k3": "kS3",
    "01": "0L3",
    "02": "1L3",
    "03": "0L2",
    "11": "1L2",
    "12": "0L3",
    "13": "1L2",
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

    return "".join(m)


print(f("1" * 57))
