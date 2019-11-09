'''
@Date: 2019-11-09 23:09:58
@Author: ywyz
@LastModifiedBy: ywyz
@Github: https://github.com/ywyz
@LastEditors: ywyz
@LastEditTime: 2019-11-09 23:16:51
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

for x in range(-100, 100):
    turtle.goto(x, math.pow(x, 2))
    turtle.pendown()

turtle.done()