# Задание 25

## Алгоритм поиска делителей

```
def div(x):
    d = set()
    for i in range(1, int(x ** 0.5) + 1):
        if x % i == 0:
            d |= { i, x // i }
    return sorted(d)
```

## Пример кода для маски

### Первый варинт
```
from fnmatch import *

for x in range(0, 10 ** 9, 169):
    if fnmatch(str(x), "345*789?"):
        print(x, x // 169)
```

### Второй вариант

```
for c1 in range(0, 10):
    x = int(f"345789{c1}")
    if x % 169 == 0:
        print(x, x // 169)
for c1 in range(0, 10):
    for c2 in range(0, 10):
        x = int(f"345{c1}789{c2}")
        if x % 169 == 0:
            print(x, x // 169)
for c1 in range(0, 10):
    for c2 in range(0, 10):
        for c3 in range(0, 10):
            x = int(f"345{c1}{c2}789{c3}")
            if x % 169 == 0:
                print(x, x // 169)
```