def f(n):
    m = bin(n)[2:]
    m += bin(n % 3)[2:].zfill(2)
    r = int(m, 2)
    m += bin(r % 5)[2:].zfill(3)

    return int(m, 2)


for i in range(1000):
    print(f(i))
