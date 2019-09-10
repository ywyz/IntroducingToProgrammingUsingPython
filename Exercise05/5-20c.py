'''
@Date: 2019-09-10 20:36:03
@Author: ywyz
@LastModifiedBy: ywyz
@Github: https://github.com/ywyz
@LastEditors: ywyz
@LastEditTime: 2019-09-10 20:41:39
'''
for number in range(1, 7):
    spacenumber = 6 - number
    while spacenumber >= 0:
        print(" ", end=" ")
        spacenumber -= 1
    n = number
    while n > 0:
        print(n, end=" ")
        n -= 1
    print("\n")
