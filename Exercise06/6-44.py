'''
@Date: 2019-11-26 20:00:22
@Author: ywyz
@LastModifiedBy: ywyz
@Github: https://github.com/ywyz
@LastEditors: ywyz
@LastEditTime: 2019-11-26 20:05:17
'''
import turtle
from math import pow

from UsefulTurtleFunctions import drawLine

drawLine(-200, 0, 200, 0)
drawLine(175, 15, 200, 0)
drawLine(200, 0, 175, -15)
drawLine(0, 200, 0, -200)
drawLine(-15, 175, 0, 200)
drawLine(0, 200, 15, 175)
turtle.penup()

for x in range(-100, 100):
    turtle.goto(x, pow(x, 2))
    turtle.pendown()

turtle.done()