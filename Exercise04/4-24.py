'''
@Date: 2019-08-24 19:40:58
@Author: ywyz
@LastModifiedBy: ywyz
@Github: https://github.com/ywyz
@LastEditors: ywyz
@LastEditTime: 2019-08-24 19:41:39
'''
import random

number = random.randint(1, 13)
color = random.randint(0, 3)

if number == 1:
    number = "Ace"
elif number == 11:
    number = "Jack"
elif number == 12:
    number = "Queen"
elif number == 13:
    number == "King"

if color == 0:
    color = " Plum"
elif color == 1:
    color = "Hearts"
elif color == 2:
    color = "Square"
else:
    color = "Spades"

print("THe card you picked is the " + str(number) + " of " + color)
