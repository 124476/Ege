a = [int(x) for x in open("txt_task_9.txt")]
d = []
mx = max([x for x in a if x % 19 == 0])

for i in range(len(a) - 1):
    if a[i] > mx or a[i + 1] > mx:
        d += [a[i] + a[i + 1]]

print(len(d), min(d))