'''
@Date: 2019-11-26 19:35:42
@Author: ywyz
@LastModifiedBy: ywyz
@Github: https://github.com/ywyz
@LastEditors: ywyz
@LastEditTime: 2019-11-26 19:49:33
'''
import turtle
from math import pi, sin

from UsefulTurtleFunctions import drawLine, writeText

drawLine(-200, 0, 200, 0)
drawLine(175, 15, 200, 0)
drawLine(200, 0, 175, -15)
drawLine(0, 200, 0, -200)
drawLine(-15, 175, 0, 200)
drawLine(0, 200, 15, 175)
turtle.penup()
for x in range(-175, 176):
    turtle.goto(x, 50 * sin((x / 100) * 2 * pi))
    turtle.pendown()

writeText("-2\u03c0", -100, -15)
writeText("2\u03c0", 100, -15)

turtle.done()
