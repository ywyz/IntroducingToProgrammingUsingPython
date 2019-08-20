'''
@Date: 2019-08-20 09:22:24
@Author: ywyz
@LastModifiedBy: ywyz
@Github: https://github.com/ywyz
@LastEditors: ywyz
@LastEditTime: 2019-08-20 09:28:36
'''
number = eval(input("Enter an integer: "))
firstNumber = number % 10
secondNumber = number // 10 % 10
thirdNumber = number // 100 % 10
fourthNumber = number // 1000
total = firstNumber * 1000 + secondNumber * 100 + thirdNumber * 10 \
       + fourthNumber
print("The reversed number is :", total)
