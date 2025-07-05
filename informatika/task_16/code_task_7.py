def f(n):
    if n <= 5: return n
    if n % 4 == 0: return n + f(n // 2 -1)
    return n + f(n + 2)


for i in range(0, 100000):
    try: print(i, f(i))
    except: pass
