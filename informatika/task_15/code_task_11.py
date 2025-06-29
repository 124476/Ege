# from itertools import *
#
# def f(x):
#     P = 2 <= x <= 20
#     Q = 15 <= x <= 25
#     A = a1 <= x <= a2
#     return ((not A) <= (not P)) or Q
#
# Ox = [i / 4 for i in range(1 * 4, 26 * 4 + 1)]
# m = []
#
# for a1, a2 in combinations(Ox, 2):
#     if all(f(x) == 1 for x in Ox):
#       m.append(a2 - a1)
#
# print(min(m)) # 12.75 => ответ 13 тк выколотая засчитывается

from itertools import *

t = int(input())

while t > 0:
    n = int(input())

    a = list(map(int, input().split()))

    b = max(a)
    sm = 0

    for x in permutations(a, 3):
        if x[0] + x[1] + x[2] > b and max(x[0], x[1], x[2]) < x[0] + x[1] + x[2] - max(x[0], x[1], x[2]):
            sm += 1
    print(sm // 6)

    t -= 1
