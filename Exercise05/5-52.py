'''
@Date: 2019-11-09 22:55:31
@Author: ywyz
@LastModifiedBy: ywyz
@Github: https://github.com/ywyz
@LastEditors: ywyz
@LastEditTime: 2019-11-09 23:03:22
'''
import turtle
import math

# 绘制直角坐标系
# x轴
turtle.penup()
turtle.goto(-200, 0)
turtle.pendown()
turtle.goto(200, 0)
turtle.penup()
turtle.goto(175, 15)
turtle.pendown()
turtle.goto(200, 0)
turtle.goto(175, -15)

# y轴
turtle.penup()
turtle.goto(0, 200)
turtle.pendown()
turtle.goto(0, -200)
turtle.penup()
turtle.goto(-15, 175)
turtle.pendown()
turtle.goto(0, 200)
turtle.goto(15, 175)
turtle.penup()

for x in range(-175, 176):
    turtle.goto(x, 50 * math.sin((x / 100) * 2 * math.pi))
    turtle.pendown()