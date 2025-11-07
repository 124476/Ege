sm = 0

for s in open("txt_task_8.txt"):
    a = [int(x) for x in s.split()]
    a1 = [x for x in a if a.count(x) == 1]
    a2 = [x for x in a if a.count(x) == 2]

    b0 = [x for x in a if x % 2 == 0]
    b1 = [x for x in a if x % 2 != 0]

    try:
        p0 = sum(b0) / len(b0)
    except:
        p0 = 0

    try:
        p1 = sum(b1) / len(b1)
    except:
        p1 = 0

    if (len(a2) == 2 and len(a1) == 4) + (abs(p0 - p1) > 50) == 1:
        sm += 1

print(sm)
