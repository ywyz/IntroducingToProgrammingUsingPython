'''
@Date: 2019-08-20 19:02:58
@Author: ywyz
@LastModifiedBy: ywyz
@Github: https://github.com/ywyz
@LastEditors: ywyz
@LastEditTime: 2019-08-20 19:02:58
'''
import turtle
import math

x1, y1, radius = eval(input("Enter the point of circle and radius: "))

turtle.penup()
turtle.goto(x1, y1)
turtle.circle(radius)

area = math.pi * radius**2

turtle.write(area)
