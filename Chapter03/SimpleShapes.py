'''
@Date: 2019-08-17 15:45:02
@Author: ywyz
@LastModifiedBy: ywyz
@Github: https://github.com/ywyz
@LastEditors: ywyz
@LastEditTime: 2019-08-17 15:45:23
'''
import turtle

turtle.pensize(3)
turtle.penup()
turtle.goto(-200, -50)
turtle.pendown()
turtle.circle(40, steps=3)

turtle.penup()
turtle.goto(-100, -50)
turtle.pendown()
turtle.circle(40, steps=4)

turtle.penup()
turtle.goto(0, -50)
turtle.pendown()
turtle.circle(40, steps=5)

turtle.penup()
turtle.goto(100, -50)
turtle.pendown()
turtle.circle(40, steps=6)

turtle.penup()
turtle.goto(200, -50)
turtle.pendown()
turtle.circle(40)

turtle.done()
