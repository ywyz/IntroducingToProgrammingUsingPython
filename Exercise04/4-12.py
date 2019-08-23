'''
@Date: 2019-08-23 09:24:25
@Author: ywyz
@LastModifiedBy: ywyz
@Github: https://github.com/ywyz
@LastEditors: ywyz
@LastEditTime: 2019-08-23 09:36:17
'''
integer = eval(input("Enter an integer: "))

if integer % 5 == 0 and integer % 6 == 0:
    print("Is", integer, "divisible by 5 and 6?:  True")
elif integer % 5 == 0 or integer % 6 == 0:
    print("Is", integer, "divisible by 5 or 6?:  True ")
    print("Is", integer, "divisible or 5 or 6, but not both?:  True")
else:
    print("Is", integer, "divisible by 5 or  6?:  False ")
