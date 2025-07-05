from turtle import *

tracer(0)
r = 20
screensize(5000, 5000)

seth(90)
rt(180)
fd(5 * r)
rt(90)
fd(50 * r)
rt(90)
fd(5 * r)
for i in range(5):
    seth(90)
    circle(-5 * r, 180)

up()
for x in range(-100, 50):
    for y in range(-50, 50):
        goto(x * r, y * r)
        dot(3, "red")

update()
mainloop()