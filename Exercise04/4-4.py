'''
@Date: 2019-08-22 12:53:07
@Author: ywyz
@LastModifiedBy: ywyz
@Github: https://github.com/ywyz
@LastEditors: ywyz
@LastEditTime: 2019-08-22 15:23:31
'''
import random

number1 = random.randrange(0, 100)
number2 = random.randrange(0, 100)

answer = number1 + number2
UserAnswer = eval(input("What is " + str(number1) + "+" + str(number2) + " ?"))
if (UserAnswer == answer):
    print("The answer is correct!")
else:
    print("Wrong!")
