'''
@Date: 2019-08-26 20:55:29
@Author: ywyz
@LastModifiedBy: ywyz
@Github: https://github.com/ywyz
@LastEditors: ywyz
@LastEditTime: 2019-08-26 20:56:13
'''
import turtle
import math

x1, y1, width1, height1 = eval(
    input("Enter r1's center x- and y-coordinates,width, and height: "))
x2, y2, width2, height2 = eval(
    input("Enter r2's center x- and y-coordinates,width, and height: "))

width = math.fabs(x2 - x1)
height = math.fabs(y2 - y1)

turtle.penup()
turtle.goto(x1 + width1 / 2, y1 + height1 / 2)
turtle.pendown()
turtle.goto(x1 + width1 / 2, y1 - height1 / 2)
turtle.goto(x1 - width1 / 2, y1 - height1 / 2)
turtle.goto(x1 - width1 / 2, y1 + height1 / 2)
turtle.goto(x1 + width1 / 2, y1 + height1 / 2)

turtle.penup()
turtle.goto(x2 + width2 / 2, y2 + height2 / 2)
turtle.pendown()
turtle.goto(x2 + width2 / 2, y2 - height2 / 2)
turtle.goto(x2 - width2 / 2, y2 - height2 / 2)
turtle.goto(x2 - width2 / 2, y2 + height2 / 2)
turtle.goto(x2 + width2 / 2, y2 + height2 / 2)

turtle.penup()
turtle.goto(max(x1, x2) + 20, max(y1, y2))
turtle.pendown()

if (width > ((width1 + width2) / 2)):
    turtle.write("r2 does not overlap r1.")
elif ((width < ((width1 + width2) / 2)) and (width > math.fabs(
    (width1 - width2) / 2))):
    if height > ((height1 + height2) / 2):
        turtle.write("r2 does not overlap r1.")
    elif (height < ((height1 + height2) / 2)) and (height > math.fabs(
        (height1 - height2) / 2)):
        turtle.write("r2 overlap r1.")
    elif (height < math.fabs((height1 - height2) / 2)):
        turtle.write("r2 overlap r1.")
elif width >= math.fabs((width1 - width2) / 2):
    if height > ((height1 + height2) / 2):
        turtle.write("r2 does not overlap r1.")
    elif (height < ((height1 + height2) / 2)) and (height > math.fabs(
        (height1 - height2) / 2)):
        turtle.write("r2 overlap r1.")
    elif (height < math.fabs((height1 - height2) / 2)):
        turtle.write("r2 is inside r1.")

turtle.done()
