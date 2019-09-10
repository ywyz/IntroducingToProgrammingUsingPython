'''
@Date: 2019-09-10 20:42:34
@Author: ywyz
@LastModifiedBy: ywyz
@Github: https://github.com/ywyz
@LastEditors: ywyz
@LastEditTime: 2019-09-10 20:55:21
'''
for number in range(1, 7):
    spacenumber = number - 1
    while spacenumber > 0:
        print(" ", end=" ")
        spacenumber -= 1
    for n in range(1, 8 - number):
        print(n, end=" ")

    print("\n")
