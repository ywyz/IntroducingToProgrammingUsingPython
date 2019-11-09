'''
@Date: 2019-11-09 20:43:16
@Author: ywyz
@LastModifiedBy: ywyz
@Github: https://github.com/ywyz
@LastEditors: ywyz
@LastEditTime: 2019-11-09 20:52:15
'''
import turtle
import random

turtle.penup()
turtle.goto(-60, 50)
turtle.pendown()

turtle.forward(120)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(120)
turtle.right(90)
turtle.forward(100)

for n in range(10):
    x = random.randrange(-60, 60)
    y = random.randrange(-50, 50)
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color("red")
    turtle.begin_fill()
    turtle.circle(5)
    turtle.end_fill()