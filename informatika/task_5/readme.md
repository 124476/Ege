# Задание 5

## Пример кода

```
def f(n):
    m = bin(n)[2:]
    if m.count("1") % 2 == 0: m += "0"
    else: m += "1"

    if m.count("1") % 2 == 0: m += "0"
    else: m += "1"

    return int(m, 2)


d = []
for i in range(1, 100):
    r = f(i)

    if r > 130:
        d += [r]

print(min(d))
```

## Части кода

### Перевод из cc (<= 10)

```
def cc(x, p):
    a = ""
    
    while x > 0:
        a = str(x % p) + a
        x //= p
        
    return a
```

### Перевод из cc (<= 36)

```
def cc(x, p):
    a = ""
    q = "0123456789" + "".join([chr(i) for i in range(ord("a"), ord("z") + 1)])

    while x > 0:
        a = q[x % p] + a
        x //= p

    return a
```

### Суммирование

#### 2сс
```
k = m.count("1")
```

#### <= 10cc

```
k = sum(map(int, m))
```

#### 16cc (до 36)

```
k = sum([int(x, 16) for x in m])
```