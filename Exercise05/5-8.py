'''
@Date: 2019-09-04 20:48:18
@Author: ywyz
@LastModifiedBy: ywyz
@Github: https://github.com/ywyz
@LastEditors: ywyz
@LastEditTime: 2019-11-10 00:07:04
'''
import math
print("------------------------------ ------------------------------")
print("        Number         |         Square Root          ")
number = 0
while number <= 20:
    print(format(number, "15d"), "       |        ",
          format(math.sqrt(number), "15.4f"))
    number += 1
