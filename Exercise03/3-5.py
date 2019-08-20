'''
@Date: 2019-08-18 20:55:28
@Author: ywyz
@LastModifiedBy: ywyz
@Github: https://github.com/ywyz
@LastEditors: ywyz
@LastEditTime: 2019-08-18 20:55:28
'''
import math

number = eval(input("Enter the number of sides: "))
side = eval(input("Enter the side: "))
Area = (number * side**2) / (4 * math.tan(math.pi / number))
print("The area of the polygon is ", Area)
