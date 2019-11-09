'''
@Date: 2019-11-09 21:58:48
@Author: ywyz
@LastModifiedBy: ywyz
@Github: https://github.com/ywyz
@LastEditors: ywyz
@LastEditTime: 2019-11-09 22:42:17
'''
import turtle
# 题目
line = ""
turtle.write("Multiplication Table", font=("Courier", 14, "bold"))
turtle.penup()
turtle.goto(0, -15)
turtle.pendown()
# 第一行数字
for n in range(1, 10):
    line += str(n) + "       "
turtle.write(line, font=("Courier", 14, "bold"))
turtle.penup()
turtle.goto(-20, -30)
turtle.pendown()
# 分隔符
turtle.write(12 * "---")
turtle.penup()
y = -45
turtle.goto(-20, y)
turtle.pendown()
for j in range(1, 10):
    line = str(j) + " | "
    for l in range(1, 10):
        if j * l > 9:
            line += str(j * l) + "     "
        else:
            line += str(j * l) + "       "
    turtle.write(line, font=("Courier", 14, "bold"))
    y -= 15
    turtle.penup()
    turtle.goto(-20, y)
    turtle.pendown()
turtle.done()
