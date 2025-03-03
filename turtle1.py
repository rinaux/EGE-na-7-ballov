from turtle import *
m = 10
screensize(2000, 2000)
tracer(0)
left(90)
forward(61*m)
right(90)
forward(61*m)
right(135)
forward(87*m)

'''right(45)
for _ in range(7):
    forward(6*m)
    right(45)
    forward(12*m)
    right(135)'''
    
up()
for x in range(-2, 70):
    for y in range(-2, 70):
        goto(x*m, y*m)
        dot(3)
update()
Screen().exitonclick()
