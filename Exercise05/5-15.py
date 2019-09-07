'''
@Date: 2019-09-07 09:30:30
@Author: ywyz
@LastModifiedBy: ywyz
@Github: https://github.com/ywyz
@LastEditors: ywyz
@LastEditTime: 2019-09-07 09:30:45
'''
import math
n = 0
while math.pow(n, 3) < 12000:
    n += 1
print(n - 1, "的立方小于12000.")
