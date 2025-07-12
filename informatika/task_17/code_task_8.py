a = [int(x) for x in open("txt_task_8.txt")]
d = []

for i in range(len(a) - 1):
    if a[i] + a[i + 1] >= 100 and (a[i] < 0 or a[i + 1] < 0):
        d += [a[i] * a[i + 1]]

print(len(d), max(d))