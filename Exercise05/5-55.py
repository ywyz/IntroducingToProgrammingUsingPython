'''
@Date: 2019-11-09 23:22:07
@Author: ywyz
@LastModifiedBy: ywyz
@Github: https://github.com/ywyz
@LastEditors: ywyz
@LastEditTime: 2019-11-09 23:48:30
'''
import turtle
turtle.pensize(10)
# 正方形
turtle.goto(400, 0)
turtle.goto(400, -400)
turtle.goto(0, -400)
turtle.goto(0, 0)

turtle.pensize(1)
x = 0
y = 0
# 行
for n in range(4):
    # 列
    for line in range(4):
        for edge in range(4):
            turtle.forward(50)
            turtle.right(90)

        turtle.penup()
        x += 50
        turtle.goto(x, y)
        turtle.pendown()

        turtle.begin_fill()
        for edge in range(4):
            turtle.fillcolor("black")
            turtle.forward(50)
            turtle.right(90)
        turtle.end_fill()

        x += 50
        turtle.goto(x, y)

    x = 0
    y -= 50
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()

    for line in range(4):
        turtle.begin_fill()
        for edge in range(4):
            turtle.fillcolor("black")
            turtle.forward(50)
            turtle.right(90)
        turtle.end_fill()

        for edge in range(4):
            turtle.forward(50)
            turtle.right(90)

        turtle.penup()
        x += 50
        turtle.goto(x, y)
        turtle.pendown()

        x += 50
        turtle.goto(x, y)

    x = 0
    y -= 50
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
