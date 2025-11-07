# Задание 2

## Логические операции в Python

- Отрицание not (a)
- Конъюнкция a and b
- Дизъюнкция a or b
- Импликация a <= b
- Эквиваленция a == b

## Пример кода

```
print("x y w z")
for x in range(2):
    for y in range(2):
        for w in range(2):
            for z in range(2):
                f = not (z and not w) or ((z <= w) == (x <= y))
                if f == 0:
                    print(x, y, w, z)
```

## Пример кода полного перебора, без аналитического анализа

```
from itertools import *

def f(x, y, z):
    return (x <= y) and (y <= z)

table = [(1, 0, 0), (1, 0, 1)]

for p in permutations("xyz"):
    if [f(**dict(zip(p, row))) for row in table]==[0,1]:
        print(p)
```

## Пример кода полного перебора с неизвестными полями, без аналитического анализа

```
from itertools import *

def f(x, y, w, z):
    return (x == (not y)) <= ((x and w) == z)

for a1, a2, a3, a4, a5 in product([0, 1], repeat=5):
    table = [(1, 1, a1, a2), (1, 1, a3, 1), (a4, 1, 1, a5)]

    if len(table) != len(set(table)):
        continue

    for p in permutations("xywz"):
        if [f(**dict(zip(p, row))) for row in table] == [0, 0, 0]:
            print(p)
```