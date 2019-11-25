'''
@Date: 2019-11-25 20:23:45
@Author: ywyz
@LastModifiedBy: ywyz
@Github: https://github.com/ywyz
@LastEditors: ywyz
@LastEditTime: 2019-11-25 20:30:18
'''
import math


def area(n, side):
    s = (n * side**2) / (4 * math.tan(math.pi / n))
    return s


def main():
    number = eval(input("Enter the number of sides: "))
    side = eval(input("Enter the side: "))
    print("The area of the polygon is ", area(number, side))


main()
