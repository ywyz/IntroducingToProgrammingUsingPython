'''
@Date: 2019-09-07 15:51:47
@Author: ywyz
@LastModifiedBy: ywyz
@Github: https://github.com/ywyz
@LastEditors: ywyz
@LastEditTime: 2019-09-07 19:22:04
'''
firstNumber = ord("!")
lastNumber = ord("~")
n = 1
for i in range(firstNumber, lastNumber + 1):
    if n % 10 == 0:
        print(chr(i))
        n = 1
    else:
        print(chr(i), end=" ")
        n += 1
