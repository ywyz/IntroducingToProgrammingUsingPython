'''
@Date: 2019-11-09 17:30:06
@Author: ywyz
@LastModifiedBy: ywyz
@Github: https://github.com/ywyz
@LastEditors: ywyz
@LastEditTime: 2019-11-09 18:40:18
'''
import random

numbersOfHits = 0
NUMBEROFTRAILS = 1000000
for n in range(NUMBEROFTRAILS):
    x = random.random() * 2.0 - 1
    y = random.random() * 2.0 - 1
    if x < 0:
        numbersOfHits += 1

    elif x > 0 and y > 0:
        y1 = -x + 1
        if y < y1:
            numbersOfHits += 1

print(numbersOfHits / NUMBEROFTRAILS)
