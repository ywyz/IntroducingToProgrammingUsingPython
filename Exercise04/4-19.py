'''
@Date: 2019-08-23 19:07:30
@Author: ywyz
@LastModifiedBy: ywyz
@Github: https://github.com/ywyz
@LastEditors: ywyz
@LastEditTime: 2019-08-23 19:26:25
'''
a, b, c = eval(input("Enter three edges: "))

if (a + b > c) and (a + c > b) and (b + c > a):
    sides = a + b + c
    print("The perimeter is ", sides)
else:
    print("The input is invild.")
