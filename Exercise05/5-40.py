'''
@Date: 2019-11-06 20:58:01
@Author: ywyz
@LastModifiedBy: ywyz
@Github: https://github.com/ywyz
@LastEditors: ywyz
@LastEditTime: 2019-11-06 21:04:03
'''
import random
positive = 0
negative = 0
for n in range(0, 1000000):
    number = random.randint(0, 1)
    if number == 0:
        positive += 1
    else:
        negative += 1

print("Positive: ", positive)
print("Negative:", negative)
