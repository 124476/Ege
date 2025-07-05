# Задание 16

Задание на рекурсию

## Пример кода

```
from functools import *


@lru_cache(None)
def f(n):
    if n == 1: return 1
    return f(n - 1) + 3 * g(n - 1)


def g(n):
    if n == 1: return 1
    return f(n - 1) - 2 * g(n - 1)


s = f(50)

print(sum([int(x) for x in str(s)]))
```


## Увеличение глубины рекурсии

```
from functools import *


@lru_cache(None)
def f(n):
    if n < -100000: return 1
    if n > 10: return f(n - 1) + 3 * f(n - 3) + 2
    return -f(n - 1)


for i in range(-100000, 20):
    f(i)

print(f(20))
```