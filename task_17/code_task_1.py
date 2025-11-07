# Первый вариант

a = [int(x) for x in open("txt_task_1.txt")]
d = []

for i in range(len(a)):
    if a[i] % 3 == 0 and a[i] % 7 != 0 and a[i] % 17 != 0 and a[i] % 19 != 0 and a[i] % 27 != 0:
        d += [a[i]]

print(len(d), max(d))

# Второй вариант

a = [int(x) for x in open("txt_task_1.txt")]
d = [x for x in a if x % 3 == 0 and x % 7 != 0 and x % 17 != 0 and x % 19 != 0 and x % 27 != 0]

print(len(d), max(d))