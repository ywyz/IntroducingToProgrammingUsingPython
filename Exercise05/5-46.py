'''
@Date: 2019-11-09 19:49:33
@Author: ywyz
@LastModifiedBy: ywyz
@Github: https://github.com/ywyz
@LastEditors: ywyz
@LastEditTime: 2019-11-09 20:41:21
'''
import math

NNUMBER = 10
total = 0
squareTotal = 0
for n in range(NNUMBER):
    number = eval(input("Enter ten numbers: "))
    total += number
    squareTotal += number**2

mean = total / NNUMBER
deviation = ((squareTotal - total * total / NNUMBER) / (NNUMBER - 1))**0.5
print("The mean is ", mean)
print("The standard deviation is ", deviation)
