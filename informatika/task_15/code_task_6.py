def f(x, y, z):
    return (220 != y + 2 * x + z) or (a < 6 * x) or (a < y) or (a < 2 * z)

for a in range(100, 1000):
    if all(f(x, y, z) for x in range(200) for y in range(200) for z in range(200)):
        print(a)