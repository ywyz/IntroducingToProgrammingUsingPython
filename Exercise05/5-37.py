'''
@Date: 2019-11-06 19:53:16
@Author: ywyz
@LastModifiedBy: ywyz
@Github: https://github.com/ywyz
@LastEditors: ywyz
@LastEditTime: 2019-11-06 19:56:17
'''
import math
total = 0
for n in range(1, 625):
    number = math.sqrt(n) + math.sqrt(n + 1)
    total += (1 / number)

print(total)
