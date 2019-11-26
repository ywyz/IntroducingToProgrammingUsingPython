'''
@Date: 2019-11-26 17:48:12
@Author: ywyz
@LastModifiedBy: ywyz
@Github: https://github.com/ywyz
@LastEditors: ywyz
@LastEditTime: 2019-11-26 19:34:18
'''
from random import randint
from UsefulTurtleFunctions import drawCircle
from UsefulTurtleFunctions import drawRectangle
from UsefulTurtleFunctions import drawPoint
import turtle

drawRectangle(-75, 0, 100, 100)
drawCircle(50, 0, 50)
point = 0
while point < 10:
    x = randint(-75, -25)
    y = randint(-50, 50)
    drawPoint(x, y)
    point += 1

point = 0
while point < 10:
    x = randint(0, 100)
    y = randint(-50, 50)
    if ((x - 50) * (x - 50) + y * y)**0.5 <= 50:
        drawPoint(x, y)
        point += 1

turtle.done()
