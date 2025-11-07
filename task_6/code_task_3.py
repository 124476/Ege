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