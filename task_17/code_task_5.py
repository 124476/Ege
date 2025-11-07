a = [int(x) for x in open("txt_task_5.txt")]
d = []

for i in range(len(a) - 2):
    if a[i] % 3 == 2 or a[i + 1] % 3 == 2 or a[i + 2] % 3 == 2:
        d += [min(a[i], a[i + 1], a[i + 2])]

print(len(d), sum(d))