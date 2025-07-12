f = open("txt_task_13.txt")
n = int(f.readline())

a = [0] * 2_000_000
for i in range(n):
    st, en = [int(x) for x in f.readline().split()]
    a[st - 1] += 1
    a[en - 1] -= 1

# n = 7
# d = [[10, 40], [50, 130], [75, 90], [120, 170], [140, 170], [150, 180]]
# a = [0] * 2_000_000
# for i in d:
#     st, en = i
#     a[st - 1] += 1
#     a[en - 1] -= 1


p = 0

for i in range(2_000_000):
    p += a[i]

    if a[i] <= 0:
        a[i] = p

    lt = a[i]

p = 0
t = True
for i in range(1, 2_000_000):
    if a[i] != 0 and t:
        p += 1
        t = False
    elif a[i] == 0:
        t = True

print(p, len([x for x in a if x > 0]))
