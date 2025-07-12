f = open("txt_task_16.txt")
n = int(f.readline())

a = []
for i in range(n):
    a += [int(f.readline())]

# n = 5
# a = [7, 1, 3, 14, 1]

mx = sum(a)

d = [0] * mx

a.sort()

d[a[0] - 1] = 1

for i in a[1:]:
    q = d.copy()
    for j in range(len(d)):
        if d[j] == 1:
            q[j + i] = 1
    q[i - 1] = 1
    d = q

mx = 0
for i in range(len(d)):
    if d[i] == 0:
        mx = i

print(d.count(0), mx + 1)
