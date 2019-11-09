'''
@Date: 2019-11-09 20:58:29
@Author: ywyz
@LastModifiedBy: ywyz
@Github: https://github.com/ywyz
@LastEditors: ywyz
@LastEditTime: 2019-11-09 21:06:21
'''
import turtle
x = 0
y = 0
radius = 50
for n in range(10):
    turtle.circle(radius)
    turtle.penup()
    y -= 10
    turtle.goto(x, y)
    turtle.pendown()
    radius += 10