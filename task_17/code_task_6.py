a = [int(x) for x in open("txt_task_6.txt")]
d = []

for i in range(len(a) - 3):
    if a[i] > a[i + 1] > a[i + 2] > a[i + 3] and max(a[i], a[i + 1], a[i + 2], a[i + 3]) - min(a[i], a[i + 1], a[i + 2], a[i + 3]) > 1000:
        d += [sum([a[i], a[i + 1], a[i + 2], a[i + 3]])]

print(len(d), min(d))