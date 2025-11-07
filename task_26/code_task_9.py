f = open("txt_task_9.txt")
n, s = map(int, f.readline().split())

a = []
for i in range(n):
    a += [int(f.readline())]

# n, s = 6, 500
# a = [140, 150, 160, 200, 220, 240]

a.sort(reverse=True)

b = []

while a:
    p = []

    k = 0
    while sum(p) <= s and k < len(a):
        if sum(p) + a[k] <= s:
            p += [a.pop(k)]
        else:
            k += 1

    b += [p]

print(len(b), sum(b[-1]))
