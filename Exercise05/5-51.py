'''
@Date: 2019-11-09 22:49:00
@Author: ywyz
@LastModifiedBy: ywyz
@Github: https://github.com/ywyz
@LastEditors: ywyz
@LastEditTime: 2019-11-09 22:54:01
'''
import turtle
LINENUMBER = 19

x = 0
y = 0

# 竖线
for line in range(LINENUMBER):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.goto(x, y + 360)
    x += 20
    y = 0

# 横线
x = 0
y = 0
for line in range(LINENUMBER):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.goto(x + 360, y)
    x = 0
    y += 20
