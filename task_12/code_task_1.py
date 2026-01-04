mp = {
    (" ", 0): (" ", -1, 1),
    (" ", 1): (" ", 2, 1),
    ("0", 1): ("1", -1, 1),
    ("1", 1): ("0", -1, 1),
}  # команды


def f(m):
    a = list(" " + m + " ")

    q = 0
    i = len(a) - 1

    while True:
        c = mp[(a[i], q)]
        a[i] = c[0]
        if c[1] == 2: break
        i += c[1]
        q = c[2]

    return "".join(a)


print(f("101110111"))
