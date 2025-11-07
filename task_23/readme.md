# Задание 23

Задание на переход числа с помощью команд

## Пример кода

### Рекурсия

```
def f(c, e):
    if c > e: return 0
    if c == e: return 1
    return f(c + 1, e) + f(c * 2, e)


print(f(2, 10))
```

### Диманика

```
a = [0] * 100
a[2] = 1
for i in range(2, 10):
    if i + 1 <= 10: a[i + 1] += a[i]
    if 2 * i <= 10: a[i * 2] += a[i]

print(a[10])
```

### Меморизация

```
from functools import *


@lru_cache(None)
def f(c, e, d):
    if c > e: return 0
    if c == e: return 12 in d
    return f(c + 1, e, d + (c,)) + f(c * 2, e, d + (c,))

print(f(1, 30, (1,)))
```