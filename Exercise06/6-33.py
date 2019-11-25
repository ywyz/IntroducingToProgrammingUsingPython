'''
@Date: 2019-11-25 20:20:47
@Author: ywyz
@LastModifiedBy: ywyz
@Github: https://github.com/ywyz
@LastEditors: ywyz
@LastEditTime: 2019-11-25 20:23:03
'''
import math


def area(s):
    area = (5 * s**2) / (4 * math.tan(math.pi / 5))

    return area


def main():
    side = eval(input("Enter the number of sides: "))
    print("The area of the pentagon is ", area(side))


main()
