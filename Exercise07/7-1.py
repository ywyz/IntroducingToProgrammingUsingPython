'''
@Date: 2019-12-01 19:43:22
@Author: ywyz
@LastModifiedBy: ywyz
@Github: https://github.com/ywyz
@LastEditors: ywyz
@LastEditTime: 2019-12-01 19:52:50
'''


class Rectangle:
    def __init__(self, width=1, height=2):
        self.width = width
        self.height = height

    def getArea(self):
        return self.width * self.height

    def getPerimeter(self):
        return self.width * 2 + self.height * 2


def main():
    width = 4
    height = 40
    rectangle1 = Rectangle(width, height)
    print("The rectangle's width is ", width)
    print("The rectangle's height is ", height)
    print("The rectangle's area is ", rectangle1.getArea())
    print("The rectangle's perimeter is ", rectangle1.getPerimeter())

    width = 3.5
    height = 35.7
    rectangle2 = Rectangle(width, height)
    print("The rectangle's width is ", width)
    print("The rectangle's height is ", height)
    print("The rectangle's area is ", rectangle2.getArea())
    print("The rectangle's perimeter is ", rectangle2.getPerimeter())


main()
