'''
@Date: 2019-11-25 20:52:23
@Author: ywyz
@LastModifiedBy: ywyz
@Github: https://github.com/ywyz
@LastEditors: ywyz
@LastEditTime: 2019-11-25 20:57:08
'''
import turtle
from random import randint


def getRandomCharacter(ch1, ch2):
    return chr(randint(ord(ch1), ord(ch2)))


def main():
    x = 0
    y = 0
    temp = 1
    tempWord = 'A'
    for n in range(100):
        tempWord = getRandomCharacter('A', 'Z')
        turtle.write(tempWord)
        turtle.penup()
        x += 10
        turtle.goto(x, y)
        turtle.pendown()

        if temp % 15 == 0:
            x = 0
            y -= 10
            turtle.penup()
            turtle.goto(x, y)
            turtle.pendown()
        temp += 1


main()
