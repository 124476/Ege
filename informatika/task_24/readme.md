# Задание 24

## Пример кода

### Перебор

```
m = open("txt_task_2.txt").readline()

p = 0

for l in range(len(m)):
    for r in range(l + p, len(m)):
        q = m[l:r + 1]
        if all(x in "123" for x in q):
            p = max(p, len(q))
        else:
            break

print(p)
```

### Регулярка
```
from re import *

m = open("txt_task_1.txt").readline()

reg = r"[ABEF]+"

d = [x.group() for x in finditer(reg, m)]

print(max([len(x) for x in d]))
```

## Регулярные выражения

### Целое число

```
num = r"([1-9][0-9]*|0)"
```