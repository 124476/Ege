# Задание 27

## Классиризация

### Через координаты x, y

```
classers = [[], [], []]
for x, y in points:
    if x > 3:
        classers[0] += [[x, y]]
    elif y >= -2.5:
        classers[1] += [[x, y]]
    else:
        classers[2] += [[x, y]]
```

### Через расстояние одной точки
```
points = []

for i in open("txt_task_1_a.txt"):
    x, y = [float(x) for x in i.replace(",", ".").split()]
    points += [[x, y]]

def dist(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

classers = []

while points:
    cl = [points.pop()]
    for p in cl:
        d = [p1 for p1 in points if dist(p, p1) < 1]
        cl += d
        for p1 in d: points.remove(p1)
    classers += [cl]
```

### Через расстояние между всеми точками

```
classers = []

while points:
    cl = [points.pop()]

    k = 0

    while k < len(cl):
        q = [p1 for p1 in points if dist(cl[k], p1) < 3]
        for p1 in q: points.remove(p1)
        cl += q
        k += 1
    
    classers += [cl]
```

## Проверка классиризации

```
from turtle import *
from random import *

tracer(0)

up()
for i in classers:
    clr = random(), random(), random()

    for x, y in i:
        goto(x * 20, y * 20)
        dot(10, clr)

update()
mainloop()
```

## Нахождение центра

```
def center(cl):
    m = []
    for p in cl:
        sm = sum(dist(p, p1) for p1 in cl)
        m += [[sm, p]]

    return min(m)[1]
```

## Последняя часть

```
centers = []
for cl in classers:
    centers += [center(cl)]

print(sum(x[0] for x in centers) / len(centers) * 10000 // 1, end=' ')
print(sum(x[1] for x in centers) / len(centers) * 10000 // 1)
```