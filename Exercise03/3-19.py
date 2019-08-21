'''
@Date: 2019-08-21 10:55:12
@Author: ywyz
@LastModifiedBy: ywyz
@Github: https://github.com/ywyz
@LastEditors: ywyz
@LastEditTime: 2019-08-21 10:58:47
'''
import turtle

x1, y1, x2, y2 = eval(input("Enter two points: "))

turtle.penup()
turtle.goto(x1, y1)
turtle.pendown()
turtle.write("(" + str(x1) + "," + str(y1) + ")")
turtle.goto(x2, y2)
turtle.write("(" + str(x2) + "," + str(y2) + ")")
turtle.hideturtle()

turtle.down()
