sm = 0

for s in open("txt_task_9.txt"):
    a = [int(x) for x in s.split()]

    b = [x for x in a if x % 3 == 0]

    if len(b) == 3 and max(a) - min(a) <= sum(b):
        sm += 1

print(sm)