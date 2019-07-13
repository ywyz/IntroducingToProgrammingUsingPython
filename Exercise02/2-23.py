'''
@Date: 2019-07-10 19:55:57
@Author: ywyz
@LastModifiedBy: ywyz
@Github: https://github.com/ywyz
@LastEditors: ywyz
@LastEditTime: 2019-07-10 19:59:06
'''
import turtle
radius = eval(input("Please enter the radius: "))

turtle.circle(radius)
turtle.penup()
turtle.goto(0, radius * 2)
turtle.pendown()
turtle.circle(radius)
turtle.penup()
turtle.goto(radius * 2, radius * 2)
turtle.pendown()
turtle.circle(radius)
turtle.penup()
turtle.goto(radius * 2, 0)
turtle.pendown()
turtle.circle(radius)
