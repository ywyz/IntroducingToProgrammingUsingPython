'''
@Date: 2019-08-26 20:59:01
@Author: ywyz
@LastModifiedBy: ywyz
@Github: https://github.com/ywyz
@LastEditors: ywyz
@LastEditTime: 2019-08-26 21:04:17
'''
import math
import turtle

x1, y1, radius1 = eval(
    input("Enter circle1's center x-, y-coordinates,and radius: "))
x2, y2, radius2 = eval(
    input("Enter circle2's center x-, y-coordinates, and radius: "))
radius = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

turtle.penup()
turtle.goto(x1, y1)
turtle.pendown()
turtle.circle(radius1)

turtle.penup()
turtle.goto(x2, y2)
turtle.pendown()
turtle.circle(radius2)

if (radius >= math.fabs(radius1 + radius2)):
    turtle.write("circle2 does not overlap circle1")
elif ((radius < math.fabs(radius1 + radius2))
      and (radius > math.fabs(radius1 - radius2))):
    turtle.write("circle2 overlaps circle1")
else:
    turtle.write("circle2 is inside circle1")

turtle.done()
