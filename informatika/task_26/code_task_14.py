f = open("txt_task_14.txt")
l, m, n = map(int, f.readline().split())

a = []
for i in range(n):
    a += [[int(x) for x in f.readline().split()]]

# l, m, n = 1200, 100, 3
# a = [[430, 300], [200, 150], [900, 50]]

a.sort()

k = 0
b = []

while a:
    st, en = a.pop(0)

    if k <= st:
        if st - k >= m:
            b += [st - k]
        k = st + en

    if k <= st + en:
        k = st + en

if k <= l and l - k >= m:
    b += [l - k]

print(len(b), max(b))
