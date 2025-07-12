f = open("txt_task_12.txt")
n = int(f.readline())

a = []
for i in range(n):
    a += [int(f.readline())]

# n = 7
# a = [4858, 112, 4858, 4858, 31, 112, 4858]

d = {}

for i in a:
    if i in d: d[i] += 1
    else: d[i] = 1

print(len(d), max(d.values()))
