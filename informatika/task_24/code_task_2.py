m = open("txt_task_2.txt").readline()

p = 0

for l in range(len(m)):
    for r in range(l + p, len(m)):
        q = m[l:r + 1]
        if all(x in "123" for x in q):
            p = max(p, len(q))
        else:
            break

print(p)