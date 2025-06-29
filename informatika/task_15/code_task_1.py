# Первый вариант
for a in range(1, 1000):
    for x in range(1, 100000):
        f = (a % 9 == 0) and ((280 % x == 0) <= ((a % x != 0) <= (730 % x != 0)))

        if f == 0: break
    else:
        print(a)

# Второй вариант
def f(x):
    return (a % 9 == 0) and ((280 % x == 0) <= ((a % x != 0) <= (730 % x != 0)))


for a in range(1, 1000):
    if all(f(x) == 1 for x in range(1, 100000)):
        print(a)
