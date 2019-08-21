'''
@Date: 2019-08-21 09:27:10
@Author: ywyz
@LastModifiedBy: ywyz
@Github: https://github.com/ywyz
@LastEditors: ywyz
@LastEditTime: 2019-08-21 11:02:30
'''
import turtle

x1, y1, x2, y2, x3, y3 = eval(input("Enter three points of the trangles: "))
a = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
b = ((x3 - x2)**2 + (y3 - y2)**2)**0.5
c = ((x3 - x1)**2 + (y3 - y1)**2)**0.5
s = (a + b + c) / 2
area = (s * (s - a) * (s - b) * (s - c))**0.5

turtle.penup()
turtle.goto(x1, y1)
turtle.pendown()
turtle.write("p1: (" + str(x1) + ", " + str(y1) + ")")
turtle.goto(x2, y2)
turtle.write("p2: (" + str(x2) + ", " + str(y2) + ")")
turtle.goto(x3, y3)
turtle.write("p3: (" + str(x3) + ", " + str(y3) + ")")
turtle.goto(x1, y1)

turtle.penup()
turtle.goto(min(x1, x2, x3), min(y1, y2, y3) - 30)
turtle.pendown()
turtle.write("The area of the trangle is : " + str(area))
