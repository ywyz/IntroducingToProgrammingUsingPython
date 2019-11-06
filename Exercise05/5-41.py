'''
@Date: 2019-11-06 21:14:38
@Author: ywyz
@LastModifiedBy: ywyz
@Github: https://github.com/ywyz
@LastEditors: ywyz
@LastEditTime: 2019-11-06 21:28:12
'''
number = eval(input("Enter a number (0 : for end of input): "))
count = 1
maxNumber = number

#去除第一个数为最大会计算两次

if maxNumber < number:
    maxNumber = number
    count = 1

while number != 0:
    number = eval(input("Enter a number (0 : for end of input): "))
    if number == 0:
        break
    elif maxNumber < number:
        maxNumber = number
        count = 1
    elif number == maxNumber:
        count += 1

    number = eval(input("Enter a number (0 : for end of input): "))

print("The largest number is ", maxNumber)
print("The occurrence count of the largest number is ", count)
