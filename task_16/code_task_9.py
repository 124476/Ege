from sys import *

setrecursionlimit(10000)

def f(n):
    if n <= 2: return 1
    if n > 2: return n * f(n - 2)


print(f(5000) / f(4994))
