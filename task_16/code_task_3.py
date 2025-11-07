def f(n):
    if n == 1: return 1
    return 2 * f(n - 1) + g(n - 1) - 2

def g(n):
    if n == 1: return 1
    return f(n - 1) + 2 * g(n - 1)

print(f(14) + g(14))
