def f(c, e, d):
    if c % 2 == 0: d += 1
    if d > 6: return 0
    if c > e: return 0
    if c == e: return d == 6
    return f(c + 1, e, d) + f(c + 3, e, d) + f(c + 5, e, d)


print(f(3, 25, 0))
