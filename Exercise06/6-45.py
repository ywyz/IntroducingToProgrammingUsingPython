'''
@Date: 2019-11-26 20:06:21
@Author: ywyz
@LastModifiedBy: ywyz
@Github: https://github.com/ywyz
@LastEditors: ywyz
@LastEditTime: 2019-11-26 20:21:40
'''
import turtle


def drawPolygon(x=0, y=0, radius=50, numberOfSides=3):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.circle(radius, steps=numberOfSides)


def main():
    drawPolygon()
    drawPolygon(x=100, numberOfSides=4)
    drawPolygon(x=200, numberOfSides=5)
    drawPolygon(x=300, numberOfSides=6)
    drawPolygon(x=400, numberOfSides=7)
    drawPolygon(x=500, numberOfSides=8)
    turtle.done()


main()
