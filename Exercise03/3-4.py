'''
@Date: 2019-08-18 20:37:47
@Author: ywyz
@LastModifiedBy: ywyz
@Github: https://github.com/ywyz
@LastEditors: ywyz
@LastEditTime: 2019-08-18 20:43:00
'''
import math

side = eval(input("Enter the number of sides: "))
area = (5 * side**2) / (4 * math.tan(math.pi / 5))
print("The area of the pentagon is ", area)
