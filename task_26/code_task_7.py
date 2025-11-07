f = open("txt_task_7.txt")
s, n = map(int, f.readline().split())
a = []
for i in range(n):
    a += [int(f.readline())]

# s, n = 100, 5
# a = [80, 30, 10, 5, 7]

b = []

while s >= sum(b):
    a = [x for x in a if sum(b) + x <= s]

    m = max(a)
    a.remove(m)
    b += [m]

    if s < sum(b) + min(a): break

    m = min(a)
    a.remove(m)
    b += [m]

print(len(b), b[-1])