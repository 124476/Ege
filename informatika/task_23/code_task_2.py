def f(c, e, step):
    if c > e: return 0
    if c == e and step == 6: return 1
    if c == e and step != 6: return 0
    return f(c + 1, e, step + 1) + f(c + 2, e, step + 1) + f(c * 2, e, step + 1)

print(f(1, 20, 0))