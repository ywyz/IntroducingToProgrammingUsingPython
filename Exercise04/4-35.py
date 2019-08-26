'''
@Date: 2019-08-26 20:28:30
@Author: ywyz
@LastModifiedBy: ywyz
@Github: https://github.com/ywyz
@LastEditors: ywyz
@LastEditTime: 2019-08-26 20:36:38
'''
import turtle
x0, y0, x1, y1, x2, y2 = eval(
    input("enter coordinates for the three points p0, p1 and p2: "))

result = (x1 - x0) * (y2 - y0) - (x2 - x0) * (y1 - y0)

turtle.penup()
turtle.goto(x0, y1)
turtle.pendown()
turtle.write("P0(" + str(x0) + "," + str(y0) + ")")
turtle.goto(x1, y1)
turtle.write("P1(" + str(x1) + "," + str(y1) + ")")

turtle.penup()
turtle.goto(x2, y2)
turtle.pendown()
turtle.dot()
turtle.write("P2")
turtle.penup()
turtle.goto(x2 - 20, y2 - 20)
turtle.pendown()
if result > 0:
    turtle.write("p2 is on the left side of the line from p0 to p1")
elif result == 0:
    turtle.write("p2 is on the same line from p0 to p1")
else:
    turtle.write("p2 is on the right side of the line from p0 to p1")
