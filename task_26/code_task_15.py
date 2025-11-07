f = open("txt_task_15.txt")
n = int(f.readline())

a = []
for i in range(n):
    a += [[int(x) for x in f.readline().split()]]

# n = 10
# a = [[1962, 1], [1962, 2], [1962, 3], [1962, 4], [1962, 6], [1962, 7], [1962, 8], [1963, 4], [1964, 1], [1964, 3]]

d = {}

for x, y in a:
    if x in d:
        d[x] |= {y}
    else:
        d[x] = {y}

mn = len(d) * 8 - sum([len(x) for x in d.values()])

p = 100
mx = 0

for i in d:
    if p >= len(d[i]):
        p = len(d[i])
        mx = i

print(mn, mx)
