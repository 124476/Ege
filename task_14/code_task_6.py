for n in range(2, 100):
    if n ** 2 <= 338 < n ** 3 and 338 % n == 2:
        print(n)