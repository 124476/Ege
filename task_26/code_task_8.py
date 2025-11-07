f = open("txt_task_8.txt")
n = int(f.readline())

a = []
for i in range(n):
    a += [int(f.readline())]

# n = 5
# a = [80, 30, 10, 50, 45]

a.sort()

b1 = []
b2 = []

while a:
    b1 += [a.pop()]

    while a and sum(b1) >= sum(b2):
        b2 += [a.pop(0)]

print(len(b1), len(b2))
