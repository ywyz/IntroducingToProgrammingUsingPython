'''
@Date: 2019-08-20 19:44:29
@Author: ywyz
@LastModifiedBy: ywyz
@Github: https://github.com/ywyz
@LastEditors: ywyz
@LastEditTime: 2019-08-20 20:31:55
'''
import turtle

turtle.penup()
turtle.goto(0, -150)
turtle.pendown()
turtle.circle(200)  # 脸

turtle.penup()  # 左眼
turtle.goto(-100, 100)
turtle.pendown()
turtle.begin_fill()
turtle.color("black")
turtle.circle(25)
turtle.end_fill()

turtle.penup()  # 右眼
turtle.goto(100, 100)
turtle.pendown()
turtle.begin_fill()
turtle.color("black")
turtle.circle(25)
turtle.end_fill()

turtle.penup()
turtle.goto(50, -50)
turtle.pendown()
turtle.setheading(60)
turtle.circle(50, steps=3)

turtle.penup()
turtle.goto(-125, -30)
turtle.pendown()
turtle.goto(0, -100)
turtle.goto(125, -30)

turtle.down()
