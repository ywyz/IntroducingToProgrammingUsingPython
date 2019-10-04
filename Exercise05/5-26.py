'''
@Date: 2019-10-04 20:14:38
@Author: ywyz
@LastModifiedBy: ywyz
@Github: https://github.com/ywyz
@LastEditors: ywyz
@LastEditTime: 2019-10-04 20:16:36
'''
number = 0
for n in range(1, 98, 2):
    number += n / (n + 2)

print(number)
