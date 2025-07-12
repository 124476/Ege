a = [int(x) for x in open("txt_task_4.txt")]
d = []

for i in range(len(a) - 2):
    if ((a[i] % 12 == 0 or a[i + 1] % 12 == 0 or a[i + 2] % 12 == 0)
            and (a[i] % 3 == 0 and a[i + 1] % 3 == 0 and a[i + 2] % 3 == 0)):
        d += [(a[i] + a[i + 1] + a[i + 2]) // 3]

print(len(d), min(d))