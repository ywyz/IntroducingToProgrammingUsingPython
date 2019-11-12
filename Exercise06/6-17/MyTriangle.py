'''
@Date: 2019-11-11 23:23:36
@Author: ywyz
@LastModifiedBy: ywyz
@Github: https://github.com/ywyz
@LastEditors: ywyz
@LastEditTime: 2019-11-11 23:31:03
'''
import math


def isVaild(side1, side2, side3):
    if side1 + side2 <= side3 or side2 + side3 <= side1 or side1 + side3 <= side2:
        return False
    else:
        return area(side1, side2, side3)


def area(side1, side2, side3):
    s = (side1 + side2 + side3) / 2
    triangleArea = math.sqrt(s * (s - side1) * (s - side2) * (s - side3))

    return triangleArea