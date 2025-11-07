sm = 0

for s in open("txt_task_7.txt"):
    a = [int(x) for x in s.split()]
    b = [x for x in a if a.count(x) != 1]

    if a.count(min(a)) == 1 and len(set(a)) != len(a) and min(a) + max(a) < sum(b):
        sm += 1

print(sm)