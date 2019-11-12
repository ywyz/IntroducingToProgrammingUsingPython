'''
@Date: 2019-11-12 00:49:11
@Author: ywyz
@LastModifiedBy: ywyz
@Github: https://github.com/ywyz
@LastEditors: ywyz
@LastEditTime: 2019-11-12 00:57:38
'''


def distance(x1, y1, x2, y2):
    length = ((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2))**0.5
    return length


def main():
    x1, y1 = eval(input("Enter x1 and y1 for Point 1: "))
    x2, y2 = eval(input("Enter x2 and y2 for Point 2: "))
    print("The distance between the two points is ", distance(x1, y1, x2, y2))


main()
