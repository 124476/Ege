# Задание 6

## Пример кода Черепашка

```
from turtle import *

r = 10 # Масштаб
tracer(0) # Мгновенная картинка
screensize(5000, 5000) # Размер окна

for i in range(2):
    fd(5 * r) # Вперед
    rt(90) # Направо
    fd(11 * r)
    rt(90)

up() # Поднять хвост

fd(-4 * r) # Назад
rt(90)
fd(6 * r)
lt(90) # Налево

down() # Опустить хвост

for i in range(2):
    fd(42 * r)
    rt(90)
    fd(63 * r)
    rt(90)

# Отрисовка точек

up()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x * r, y * r)
        dot(3, "red")

update() # Мгновенная картинка
mainloop() # Чтобы окно не закрывалось
```


## Пример кода Чертежник

```
from turtle import *

tracer(0)
r = 30
screensize(5000, 5000)


def vec(x, y):
    goto(xcor() + x * r, ycor() + y * r)


for i in range(2):
    vec(3, 4)
    vec(-3, 4)
    vec(-3, -4)
    vec(3, -4)

up()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x * r, y * r)
        dot(3, "red")

update()
mainloop()
```

## Пример кода Цапля

```
from turtle import *

tracer(0)
r = 20
screensize(5000, 5000)

rt(180)
fd(5 * r)
rt(90)
fd(50 * r)
rt(90)
fd(5 * r)
for i in range(5):
    seth(0)
    circle(-5 * r, 180)

up()
for x in range(-50, 50):
    for y in range(-50, 100):
        goto(x * r, y * r)
        dot(3, "red")

update()
mainloop()
```