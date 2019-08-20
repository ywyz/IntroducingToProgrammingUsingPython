'''
@Date: 2019-08-17 18:12:16
@Author: ywyz
@LastModifiedBy: ywyz
@Github: https://github.com/ywyz
@LastEditors: ywyz
@LastEditTime: 2019-08-18 18:03:44
'''
import math

x1, y1 = eval(input("Enter point 1 (latitude and longitude ) in degrees: "))
x2, y2 = eval(input("Enter point 2(latitude and longitude) in degrees: "))
length = 6371.01 * math.acos(
    math.sin(math.radians(x1)) * math.sin(math.radians(x2)) +
    math.cos(math.radians(x1)) * math.cos(math.radians(x2)) *
    math.cos(math.radians(y2 - y1)))

print("The distance between the two points is ", length, "km.")
