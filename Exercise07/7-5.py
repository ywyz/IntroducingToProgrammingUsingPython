'''
@Date: 2019-12-03 21:00:35
@Author: ywyz
@LastModifiedBy: ywyz
@Github: https://github.com/ywyz
@LastEditors: ywyz
@LastEditTime: 2019-12-03 21:13:54
'''
from math import pi, tan


class RegularPolygon:
    def __init__(self, n=3, side=1.0, x=0.0, y=0.0):
        self.__n = n
        self.__side = side
        self.__x = x
        self.__y = y

    def setN(self, n):
        self.__n = n

    def setSide(self, side):
        self.__side = side

    def setX(self, x):
        self.__x = x

    def setY(self, y):
        self.__y = y

    def getN(self):
        return self.__n

    def getSide(self):
        return self.__side

    def getX(self):
        return self.__x

    def getY(self):
        return self.__y

    def getArea(self):
        self.__s = self.__n * self.__side
        return self.__s

    def getPerimeter(self):
        perimeter = (self.__n * self.__s * self.__s) / (4 * tan(pi / self.__n))
        return perimeter


def display(RegularPolygon):
    print("Area is ", format(RegularPolygon.getArea(), ".2f"))

    print("Perimeter is ", format(RegularPolygon.getPerimeter(), ".2f"))


def main():
    pologyn1 = RegularPolygon()
    pologyn2 = RegularPolygon(6, 4)
    pologyn3 = RegularPolygon(10, 4, 5.6, 7.8)
    display(pologyn1)
    display(pologyn2)
    display(pologyn3)


main()
