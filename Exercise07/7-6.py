'''
@Date: 2019-12-04 17:23:45
@Author: ywyz
@LastModifiedBy: ywyz
@Github: https://github.com/ywyz
@LastEditors: ywyz
@LastEditTime: 2019-12-04 18:29:42
'''


class QuadraticEquation:
    def __init__(self, a, b, c):
        self.__a = a
        self.__b = b
        self.__c = c

    def getA(self):
        return self.__a

    def getB(self):
        return self.__b

    def getC(self):
        return self.__c

    def getDescriminant(self):
        self.__descriminant = self.__b * self.__b - 4 * self.__a * self.__c
        return self.__descriminant

    def getRoot1(self):
        if self.__descriminant >= 0:
            return (self.__b * -1 + self.__descriminant**0.5) / (self.__a * 2)

        else:
            return 0

    def getRoot2(self):
        if self.__descriminant >= 0:
            return (self.__b * -1 - self.__descriminant**0.5) / (self.__a * 2)

        else:
            return 0


def main():
    a, b, c = eval(input("Enter a, b, c:"))
    equation = QuadraticEquation(a, b, c)
    if equation.getDescriminant() < 0:
        print("The equation has no real roots.")

    elif equation.getDescriminant() == 0:
        print("The root is ", equation.getRoot1())

    else:
        print("The roots are ", equation.getRoot1(), " and ",
              equation.getRoot2())


main()
