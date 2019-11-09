'''
@Date: 2019-11-09 19:08:48
@Author: ywyz
@LastModifiedBy: ywyz
@Github: https://github.com/ywyz
@LastEditors: ywyz
@LastEditTime: 2019-11-09 19:15:52
'''
value = ""
number = eval(input("Enter a number (Decimal): "))
while number >= 2:
    n = number % 2
    value = str(n) + value
    number //= 2

value = str(number) + value
print(value)