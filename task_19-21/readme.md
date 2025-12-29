# Задание 19-21

Задание на теорию игр

## Пример кода

### Одна куча

```
def f(s, m):
    if s % 10 == 0: return m % 2 == 0
    if m == 0: return 0
    h = [f(s + 1, m - 1), f(s + 3, m - 1), f(s + 11, m - 1)]
    return any(h) if m % 2 else all(h)


print("19)", [x for x in range(10, 100) if x % 10 != 0 and f(x, 2)])
print("20)", [x for x in range(10, 100) if x % 10 != 0 and not f(x, 1) and f(x, 3)])
print("21)", sum([x for x in range(10, 100) if x % 10 != 0 and not f(x, 2) and f(x, 4)]))
```

### Две кучи
```
def f(s1, s2, lt, m):
  if s1 + s2 <= 42: return m % 2 == 0
  if m == 0: return 0
  h = []
  if s1 >= 4 and lt != 1:
    h += [f(s1 - 4, s2, 1, m - 1)]
  if s2 >= 4 and lt != 2:
    h += [f(s1, s2 - 4, 2, m - 1)]
  if lt != 3: h += [f(s1 // 3, s2, 3, m - 1)]
  if lt != 4: h += [f(s1, s2 // 3, 4, m - 1)]

  return any(h) if m % 2 else all(h)


print("19)", [x for x in range(2, 1000) if f(50, x, 0, 2)])
print("20)", [x for x in range(2, 1000) if not f(50, x, 0, 1) and f(50, x, 0, 3)])
print("21)", max([x for x in range(2, 10000) if not f(50, x, 0, 2) and f(50, x, 0, 4)]))
```
