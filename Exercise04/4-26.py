'''
@Date: 2019-08-24 21:16:23
@Author: ywyz
@LastModifiedBy: ywyz
@Github: https://github.com/ywyz
@LastEditors: ywyz
@LastEditTime: 2019-08-26 16:34:04
'''
number = eval(input("Enter a three-digit integer: "))
lastNumber = number % 10
firstNumber = number // 100
if lastNumber == firstNumber:
    print(number, "is a palindrome.")
else:
    print(number, "is not a palindrone")
