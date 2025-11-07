# Задание 1

Задание на графы

## Пример кода

```
from itertools import *

a = '57 457 46 236 12 348 128 67'.split() # Таблица
s = 'CF FA FB AE EB BD DH DG HG CG'.split() # Соединение между букв
print(*range(1, 9)) # Количество дорог

for p in permutations('ABCDEFGH'): # Перебор
    if all(str(p.index(x) + 1) in a[p.index(y)] for x, y in s): # Проверка
        print(*p)
        break
```

## Пример кода (Старая версия)

```
from itertools import *

s1 = '1248 2157 3456 4136 523 634 728 817'
s2 = 'AFBE BAHE CFGH DGH EAB FAC GCD HCDB'

s2 = { i[0]: frozenset(i[1:]) for i in s2.split() }

print("1 2 3 4 5 6 7 8")
for p in permutations('ABCDEFGH'):
    s3 = s1
    for x, y in zip("12345678", p):
        s3 = s3.replace(x, y)
    s3 = { i[0]: frozenset(i[1:]) for i in s3.split() }

    if s2 == s3:
        print(*p)
```