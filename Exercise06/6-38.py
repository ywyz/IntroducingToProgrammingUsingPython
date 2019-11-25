'''
@Date: 2019-11-25 21:00:36
@Author: ywyz
@LastModifiedBy: ywyz
@Github: https://github.com/ywyz
@LastEditors: ywyz
@LastEditTime: 2019-11-25 21:05:41
'''
import turtle


def drawline(x1, y1, x2, y2, color="black", size=1):
    turtle.penup()
    turtle.goto(x1, y1)
    turtle.pencolor(color)
    turtle.pensize(size)
    turtle.pendown()
    turtle.goto(x2, y2)


def main():
    drawline(25, 65, 205, 105, "red", 6)

    turtle.done()


main()
