points = []
for i in open("txt_task_2_b.txt"):
    x, y = [float(k) for k in i.replace(",", ".").split()]
    points += [[x, y]]


def dist(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5


classers = []
while points:
    cl = [points.pop()]

    q = [p1 for p1 in points if dist(cl[0], p1) < 0.3]
    cl += q
    for p1 in q: points.remove(p1)

    k = 1
    while k < len(cl):
        q = [p1 for p1 in points if dist(cl[k], p1) < 0.3]
        cl += q
        for p1 in q: points.remove(p1)
        k += 1

    classers += [cl]

from turtle import *
from random import *

tracer(0)
up()

for cl in classers:
    clr = random(), random(), random()
    for x, y in cl:
        goto(x * 30, y * 30)
        dot(2, clr)

update()
mainloop()

def center(cl):
    m = []
    for p in cl:
        sm = sum([dist(p, p1) for p1 in cl])
        m += [[sm, p]]

    return min(m)[1]


centers = [center(cl) for cl in classers]

print(sum([p[0] for p in centers]) / len(centers) * 10000, end=' ')
print(sum([p[1] for p in centers]) / len(centers) * 10000)
