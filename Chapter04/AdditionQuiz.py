'''
@Date: 2019-08-21 17:42:01
@Author: ywyz
@LastModifiedBy: ywyz
@Github: https://github.com/ywyz
@LastEditors: ywyz
@LastEditTime: 2019-08-21 17:44:59
'''
import random

number1 = random.randint(0, 9)
number2 = random.randint(0, 9)

answer = eval(input("What is " + str(number1) + "+" + str(number2) + "? "))

print(number1, "+", number2, "=", answer, "is", number1 + number2 == answer)
