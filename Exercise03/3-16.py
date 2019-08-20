'''
@Date: 2019-08-20 20:40:04
@Author: ywyz
@LastModifiedBy: ywyz
@Github: https://github.com/ywyz
@LastEditors: ywyz
@LastEditTime: 2019-08-20 20:48:31
'''
import turtle

turtle.setheading(60)
turtle.pensize(3)
turtle.penup()
turtle.goto(-200, 0)
turtle.pendown()
turtle.begin_fill()
turtle.color("red")
turtle.circle(40, steps=3)
turtle.end_fill()

turtle.penup()
turtle.goto(-100, 0)
turtle.pendown()
turtle.begin_fill()
turtle.color("blue")
turtle.setheading(45)
turtle.circle(40, steps=4)
turtle.end_fill()

turtle.pensize(3)
turtle.penup()
turtle.goto(0, 0)
turtle.pendown()
turtle.begin_fill()
turtle.setheading(37.5)
turtle.color("green")
turtle.circle(40, steps=5)
turtle.end_fill()

turtle.pensize(3)
turtle.penup()
turtle.goto(100, 0)
turtle.pendown()
turtle.begin_fill()
turtle.color("yellow")
turtle.setheading(30)
turtle.circle(40, steps=6)
turtle.end_fill()

turtle.pensize(3)
turtle.penup()
turtle.goto(200, 0)
turtle.pendown()
turtle.begin_fill()
turtle.color("purple")
turtle.setheading(25)
turtle.circle(40, steps=8)
turtle.end_fill()
turtle.color("green")
turtle.penup()
turtle.goto(-150, 150)
turtle.pendown()
turtle.write("Cool Colorful Shapes", font=("Times", 18, "bold"))
turtle.hideturtle()

turtle.done()
