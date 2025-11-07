a = [int(x) for x in open("txt_task_3.txt")]
d = []

for x in a:
    if x % 16 == 11 and x % 7 == 0 and x % 6 != 0 and x % 13 != 0 and x % 19 != 0:
        d += [x]

print(sum(d), len(d))