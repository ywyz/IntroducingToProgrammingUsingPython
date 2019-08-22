'''
@Date: 2019-08-22 12:12:33
@Author: ywyz
@LastModifiedBy: ywyz
@Github: https://github.com/ywyz
@LastEditors: ywyz
@LastEditTime: 2019-08-22 12:12:33
'''
import random

number1 = random.randint(0, 9)
number2 = random.randint(0, 9)
number3 = random.randint(0, 9)

answer = eval(
    input("What is " + str(number1) + "+" + str(number2) + "+" + str(number3) +
          "? "))

print(number1, "+", number2, "+", number3, "=", answer, "is",
      number1 + number2 + number3 == answer)
