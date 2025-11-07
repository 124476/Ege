m = open("txt_task_7.txt").readline()

p = 0

for l in range(len(m)):
    for r in range(l + p, len(m)):
        q = m[l : r+ 1]
        if all([q[i] <= q[i + 1] for i in range(len(q) - 1)]):
            p = max(p, len(q))
        else: break

print(p)