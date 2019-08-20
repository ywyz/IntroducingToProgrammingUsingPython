'''
@Date: 2019-08-17 16:42:08
@Author: ywyz
@LastModifiedBy: ywyz
@Github: https://github.com/ywyz
@LastEditors: ywyz
@LastEditTime: 2019-08-17 16:47:54
'''
import math

lengthCenterToVertex = eval(
    input("Enter the length from the center to a vertex: "))
length = 2 * lengthCenterToVertex * (math.sin(math.pi / 5))
area = 5 * length * length / (4 * math.tan(math.pi / 5))
print("The area of the pentagon is", area)
