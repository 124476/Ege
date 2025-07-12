m = open("txt_task_4.txt").readline()

p = 0

for l in range(len(m)):
    for r in range(l + p, len(m)):
        q = m[l:r + 1]
        if "XY" not in q and "XZ" not in q:
            p = max(p, len(q))
        else: break

print(p)
