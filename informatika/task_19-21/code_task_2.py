def f(s, m):
    if 45 <= s <= 112: return m % 2 == 0
    if s > 112: return m % 2 != 0
    if m == 0: return 0
    h = [f(s + 2, m - 1), f(s * 3, m - 1)]
    return any(h) if (m - 1) % 2 == 0 else all(h)


print("19)", [x for x in range(1, 45) if f(x, 2)])
print("20)", [x for x in range(1, 45) if not f(x, 1) and f(x, 3)])
print("21)", [x for x in range(1, 45) if not f(x, 2) and f(x, 4)])
