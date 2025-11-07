a = [int(x) for x in open("txt_task_12.txt")]
d = []

def f(x):
    return x >= 0 and str(x)[-1] == "9"

for i in range(len(a) - 2):
    if not f(a[i]) and f(a[i + 1]) and not f(a[i + 2]):
        d += [a[i] + a[i + 1] + a[i + 2]]

print(len(d), max(d))