from turtle import *

tracer(0)
r = 20
screensize(5000, 5000)

for i in range(14):
    for j in range(3):
        fd(3 * r)
        rt(90)
    lt(180)

up()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x * r, y * r)
        dot(3, "red")

update()
mainloop()