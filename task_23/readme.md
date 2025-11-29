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
q = [0] * 1000

q[5] = 1
for x in range(5, 23):
    q[x + 3] += q[x]
    q[2 * x + 1] += q[x]
    q[x // 3 * 3 + 3] += q[x]

p23 = q[23]

q = [0] * 1000
q[23] = p23

for x in range(23, 100):
    q[50] = 0
    q[x + 3] += q[x]
    q[2 * x + 1] += q[x]
    q[x // 3 * 3 + 3] += q[x]

print(q[89])
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
