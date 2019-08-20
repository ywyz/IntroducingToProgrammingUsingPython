'''
@Date: 2019-08-20 09:43:28
@Author: ywyz
@LastModifiedBy: ywyz
@Github: https://github.com/ywyz
@LastEditors: ywyz
@LastEditTime: 2019-08-20 11:22:44
'''
import turtle

turtle.setheading(90)
turtle.pensize(6)
turtle.begin_fill()
turtle.color("red")
turtle.circle(100, steps=6)
turtle.end_fill()
turtle.penup()

turtle.goto(-140, -25)
turtle.pendown()
turtle.begin_fill()
turtle.color("white")
turtle.write("stop", font=("Arial", 36, "normal"))
turtle.end_fill()
turtle.hideturtle()

turtle.done()
