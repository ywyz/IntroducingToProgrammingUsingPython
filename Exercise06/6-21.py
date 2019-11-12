'''
@Date: 2019-11-12 01:02:06
@Author: ywyz
@LastModifiedBy: ywyz
@Github: https://github.com/ywyz
@LastEditors: ywyz
@LastEditTime: 2019-11-12 01:12:46
'''
from math import fabs


def sqrt(n):
    lastGuess = 1
    nestGuess = (lastGuess + (n / lastGuess)) / 2
    while fabs(lastGuess - nestGuess) > 0.0001:
        lastGuess = nestGuess
        nestGuess = (lastGuess + (n / lastGuess)) / 2

    return nestGuess


def main():
    number = eval(input("Enter a number: "))
    print("The sqrt is", sqrt(number))


main()
