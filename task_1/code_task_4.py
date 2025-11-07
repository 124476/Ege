from itertools import *

a = '57 457 46 236 12 348 128 67'.split() # Таблица
s = 'CF FA FB AE EB BD DH DG HG CG'.split() # Соединение между букв
print(*range(1, 9)) # Количество дорог

for p in permutations('ABCDEFGH'): # Перебор
    if all(str(p.index(x) + 1) in a[p.index(y)] for x, y in s): # Проверка
        print(*p)
        break
