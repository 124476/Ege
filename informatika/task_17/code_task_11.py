a = [int(x) for x in open("txt_task_11.txt")]
d = []


def f(x, y):
    return x % 9 == 0 and y % 9 != 0 and y % 8 == 3


for i in range(len(a) - 1):
    if f(a[i], a[i + 1]) or f(a[i + 1], a[i]):
        d += [max(a[i], a[i + 1])]

print(len(d), max(d))
