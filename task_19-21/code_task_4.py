def f(s, m, p):
    if s >= 140: return m % 2 == 0
    if m == 0: return 0

    h = []
    if p != "+1": h += [f(s + 1, m - 1, "+1")]
    if p != "+2": h += [f(s + 2, m - 1, "+2")]
    if p != "*3": h += [f(s * 3, m - 1, "*3")]

    return any(h) if (m - 1) % 2 == 0 else all(h)


print("19)", [x for x in range(1, 140) if f(x, 2, "")])
print("20)", [x for x in range(1, 140) if not f(x, 1, "") and f(x, 3, "")])
print("21)", [x for x in range(1, 140) if not f(x, 2, "") and f(x, 4, "")])