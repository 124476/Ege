a = [int(x) for x in open("txt_task_2.txt")]
d = []
avg = sum(a) / len(a)

for i in range(len(a) - 1):
    if a[i] > avg and a[i + 1] > avg and abs(a[i] + a[i + 1]) % 100 == 31:
        d += [a[i] + a[i + 1]]

print(len(d), max(d))
