'''
@Date: 2019-12-04 20:37:26
@Author: ywyz
@LastModifiedBy: ywyz
@Github: https://github.com/ywyz
@LastEditors: ywyz
@LastEditTime: 2019-12-04 20:51:55
'''


class linearEquation:
    def __init__(self, a, b, c, d, e, f):
        self.__a = a
        self.__b = b
        self.__c = c
        self.__d = d
        self.__e = e
        self.__f = f

    def getA(self):
        return self.__a

    def getB(self):
        return self.__b

    def getC(self):
        return self.__c

    def getD(self):
        return self.__d

    def getE(self):
        return self.__e

    def getF(self):
        return self.__f

    def isSolvable(self):
        if self.__a * self.__d - self.__b * self.__c:
            return True

        else:
            return False

    def getX(self):
        return (self.__e * self.__d - self.__b * self.__f) / (
            self.__a * self.__d - self.__b * self.__c)

    def getY(self):
        return (self.__a * self.__f - self.__e * self.__c) / (
            self.__a * self.__d - self.__b * self.__c)


def main():
    x1, y1, x2, y2 = eval(
        input("Enter the endpoints of the first line segment: "))
    x3, y3, x4, y4 = eval(
        input("Enter the endpoints of the second line segment: "))
    a = y1 - y2
    b = -1 * (x1 - x2)
    c = y3 - y4
    d = -1 * (x3 - x4)
    e = (y1 - y2) * x1 - (x1 - x2) * y1
    f = (y3 - y4) * x3 - (x3 - x4) * y3
    equation = linearEquation(a, b, c, d, e, f)

    if equation.isSolvable():
        print("The inteersecting point is at (", equation.getX(), ", ",
              equation.getY(), ")")

    else:
        print("THe two lines is parallel")


main()
