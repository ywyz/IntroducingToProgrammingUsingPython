'''
@Date: 2019-08-26 20:41:01
@Author: ywyz
@LastModifiedBy: ywyz
@Github: https://github.com/ywyz
@LastEditors: ywyz
@LastEditTime: 2019-08-26 20:45:08
'''
import turtle
x, y = eval(input("Enter the point: "))

turtle.penup()
turtle.goto(50, 25)
turtle.pendown()
turtle.goto(50, -25)
turtle.goto(-50, -25)
turtle.goto(-50, 25)
turtle.goto(50, 25)
turtle.penup()
turtle.goto(x, y)
turtle.pendown()
turtle.dot(3)

turtle.penup()
turtle.goto(-75, -50)
turtle.pendown()

if (x >= -50 and x <= 50 and y >= -25 and y <= 25):
    turtle.write("The point is inside the rectangle.")
else:
    turtle.write("The point is not inside the rectangle.")

turtle.done()
