def f(x, y):
    return (y + 3 * x < a) or (x > 20) or (y > 40)

for a in range(1, 1000):
    if all(f(x, y) == 1 for x in range(1, 100) for y in range(1, 100)):
        print(a)