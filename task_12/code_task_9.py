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


for x in "01456789":
    mp = {
        "k0": "kR1",

        "k1": "kS1",
        "21": "3R1",
        "31": f"{x}R1",
        f"{x}1": "2R1",
    }

    if sum(int(y) for y in f("2" * 764 + "3" * 122 + f"{x}" * 114)) == 3496:
        print(x)
