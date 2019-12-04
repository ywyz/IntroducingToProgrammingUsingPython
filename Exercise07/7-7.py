'''
@Date: 2019-12-04 18:59:18
@Author: ywyz
@LastModifiedBy: ywyz
@Github: https://github.com/ywyz
@LastEditors: ywyz
@LastEditTime: 2019-12-04 19:32:43
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
    a, b, c, d, e, f = eval(input("Enter a, b, c, d, e, f: "))
    equation = linearEquation(a, b, c, d, e, f)
    if equation.isSolvable():
        print("X is ", equation.getX(), "and Y is ", equation.getY())

    else:
        print("The equation has no solution.")


main()
