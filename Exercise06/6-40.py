'''
@Date: 2019-11-25 21:23:50
@Author: ywyz
@LastModifiedBy: ywyz
@Github: https://github.com/ywyz
@LastEditors: ywyz
@LastEditTime: 2019-11-25 21:33:31
'''
import turtle


def drawRectangle(color="black", x=0, y=0, width=30, height=30):
    turtle.penup()
    turtle.color(color)
    turtle.begin_fill()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.goto(x, y - height)
    turtle.goto(x + width, y - height)
    turtle.goto(x + width, y)
    turtle.goto(x, y)
    turtle.end_fill()


def drawCircle(color="black", x=0, y=0, radius=50):
    turtle.penup()
    turtle.color(color)
    turtle.begin_fill()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.circle(radius)
    turtle.end_fill()


def main():
    drawRectangle()
    drawCircle()

    turtle.done()


main()