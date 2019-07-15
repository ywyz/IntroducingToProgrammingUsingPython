'''
@Date: 2019-07-13 19:00:59
@Author: ywyz
@LastModifiedBy: ywyz
@Github: https://github.com/ywyz
@LastEditors: ywyz
@LastEditTime: 2019-07-13 19:15:55
'''
import turtle
x1, y1, length, wide = eval(
    input("Enter the center points ,length, and wide:"))
turtle.penup()
turtle.goto(x1 - length / 2, y1 - wide / 2)
turtle.pendown()
turtle.forward(length)
turtle.right(90)
turtle.forward(wide)
turtle.right(90)
turtle.forward(length)
turtle.right(90)
turtle.forward(wide)
turtle.right(90)
