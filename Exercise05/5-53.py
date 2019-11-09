'''
@Date: 2019-11-09 23:04:06
@Author: ywyz
@LastModifiedBy: ywyz
@Github: https://github.com/ywyz
@LastEditors: ywyz
@LastEditTime: 2019-11-09 23:08:04
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

# Sin函数
turtle.color("blue")
for x in range(-175, 176):
    turtle.goto(x, 50 * math.sin((x / 100) * 2 * math.pi))
    turtle.pendown()
# Cos函数
turtle.penup()
turtle.color("red")
for x in range(-175, 176):
    turtle.goto(x, 50 * math.cos((x / 100) * 2 * math.pi))
    turtle.pendown()

turtle.penup()
turtle.goto(-100, -15)
turtle.pendown()
turtle.color("black")
turtle.write("-2\u03c0")
turtle.penup()
turtle.goto(100, -15)
turtle.pendown()
turtle.write("2\u03c0")
turtle.done()
