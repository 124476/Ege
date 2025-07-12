def f(c, e, d):
    if d > 3: return 0
    if c > e: return 0
    if c == e: return 1
    return f(c + 2, e, d) + f(c * 3, e, d + 1) + f(c * 5, e, d + 1)


print(f(2, 200, 0))
