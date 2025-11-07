a = [int(x) for x in open("txt_task_13.txt")]
d = []
sm = sum([sum([int(i) for i in str(x)]) for x in a if x % 35 == 0])


def f(x, y):
    return x > sm >= y and hex(y)[-2:] == "ef"


for i in range(len(a) - 1):
    if f(a[i], a[i + 1]) + f(a[i + 1], a[i]) == 1:
        d += [a[i] + a[i + 1]]

print(len(d), min(d))
