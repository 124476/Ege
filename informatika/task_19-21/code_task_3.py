def f(a, b, m):
    if a + b >= 45: return m % 2 == 0
    if m == 0: return 0
    h = [f(a + 1, b, m - 1), f(a * 3, b, m - 1), f(a, b + 1, m - 1), f(a, b * 3, m - 1)]
    return any(h) if (m - 1) % 2 == 0 else all(h)

print("19)", [x for x in range(1, 41) if f(4, x, 2)]) # all -> меняем на any, если неудачно
print("20)", [x for x in range(1, 41) if not f(4, x, 1) and f(4, x, 3)])
print("21)", [x for x in range(1, 41) if not f(4, x, 2) and f(4, x, 4)])
