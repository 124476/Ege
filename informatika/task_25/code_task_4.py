def p(x):
    return all(x % i != 0 for i in range(2, int(x ** 0.5) + 1))

for i in range(int(106_732_567 ** 0.25), int(152_673_836 ** 0.25) + 2):
    if p(i):
        print(i ** 4, i ** 3)
