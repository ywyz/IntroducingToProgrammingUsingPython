'''
@Date: 2019-11-09 22:39:05
@Author: ywyz
@LastModifiedBy: ywyz
@Github: https://github.com/ywyz
@LastEditors: ywyz
@LastEditTime: 2019-11-09 22:48:12
'''
import turtle
x = 0
y = 0
for n in range(1, 11):
    line = ""
    for l in range(1, n + 1):
        line += str(l) + " "
    y -= 30
    turtle.penup()
    turtle.goto(x, y)
    turtle.penup()
    turtle.write(line, font=("Courier", 14, "bold"))

turtle.done()
