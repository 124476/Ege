a = [int(x) for x in open("txt_task_10.txt")]
d = []

a1 = [x for x in a if x % 11 == 0]
a2 = [x for x in a if x % 17 == 0]

if len(a1) > len(a2):
    print(len(a1), min(a1))
else:
    print(len(a2), min(a2))