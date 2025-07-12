f = open("txt_task_10.txt")
n = int(f.readline())

a = []
for i in range(n):
    a += [int(f.readline())]

# n = 8
# a = [3, 8, 14, 11, 2, 16, 5, 9]

a.sort()

mn = a[n // 2 - 1]
mx = a[n // 2 + n // 4]

b = []
for i in a:
    for j in a:
        if i <= j: continue
        if (i + j) % 2 != 0: continue
        if mn < (i + j) // 2 < mx:
            b += [(i + j) // 2]

print(len(b), min(b))