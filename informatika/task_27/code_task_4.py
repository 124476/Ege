points = []
for i in open("txt_task_4_b.txt"):
    x, y = [float(k) for k in i.replace(",", ".").split()]
    points += [[x, y]]


def dist(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return abs(x2 - x1) + abs(y2 - y1)


classers = []

while points:
    cl = [points.pop()]

    q = [p1 for p1 in points if dist(cl[0], p1) < 3]
    for p1 in q: points.remove(p1)
    cl += q

    k = 1
    while k < len(cl):
        q = [p1 for p1 in points if dist(cl[k], p1) < 3]
        for p1 in q: points.remove(p1)
        cl += q
        k += 1

    classers += [cl]

from turtle import *
from random import *

tracer(0)
up()

for cl in classers:
    clr = random(), random(), random()
    for x, y in cl:
        goto(x * 10 - 300, y * 10)
        dot(3, clr)

update()
mainloop()

def center(cl):
    m = []

    for p in cl:
        sm = sum([dist(p, p1) for p1 in cl])
        m += [[sm, p]]

    return min(m)[-1]


centers = [center(cl) for cl in classers]
print(sum([p1[0] for p1 in centers]) / len(centers) * 1000, end=' ')
print(sum([p1[1] for p1 in centers]) / len(centers) * 1000)
