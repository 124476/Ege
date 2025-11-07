def f(x, y):
    return (2 * y + 3 * x < a) or (x + y > 40)

for a in range(-100, 1000):
    if all(f(x, y) for x in range(0, 1000) for y in range(0, 1000)):
        print(a)