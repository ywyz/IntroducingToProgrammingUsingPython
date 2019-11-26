'''
@Date: 2019-11-26 19:58:17
@Author: ywyz
@LastModifiedBy: ywyz
@Github: https://github.com/ywyz
@LastEditors: ywyz
@LastEditTime: 2019-11-26 19:59:27
'''
import turtle
from math import pi, sin, cos

from UsefulTurtleFunctions import drawLine, writeText

drawLine(-200, 0, 200, 0)
drawLine(175, 15, 200, 0)
drawLine(200, 0, 175, -15)
drawLine(0, 200, 0, -200)
drawLine(-15, 175, 0, 200)
drawLine(0, 200, 15, 175)
turtle.penup()

turtle.color("blue")
for x in range(-175, 176):
    turtle.goto(x, 50 * sin((x / 100) * 2 * pi))
    turtle.pendown()
# Cos函数
turtle.penup()
turtle.color("red")
for x in range(-175, 176):
    turtle.goto(x, 50 * cos((x / 100) * 2 * pi))
    turtle.pendown()

writeText("-2\u03c0", -100, -15)
writeText("2\u03c0", 100, -15)

turtle.done()
