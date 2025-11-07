a = [int(x) for x in open("txt_task_7.txt")]
avg = sum(a) / len(a)
d = []

for i in range(len(a) - 2):
    if (a[i] > avg) + (a[i + 1] > avg) + (a[i + 2] > avg) >= 2:
        d += [a[i] + a[i + 1] + a[i + 2]]

print(len(d), max(d))