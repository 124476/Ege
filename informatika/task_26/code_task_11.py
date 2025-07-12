f = open("txt_task_11.txt")
n = int(f.readline())

a = []
for i in range(n):
    a += [int(f.readline())]

# n = 6
# a = [3, 8, 14, 11, 22, 17]
d = set(a)

a.sort()

b = []

for i in a:
    for j in a:
        if i <= j: continue
        if i % 2 == j % 2: continue
        if i + j not in d: continue
        b += [i + j]

print(len(b), max(b))
