'''
@Date: 2019-11-10 19:12:57
@Author: ywyz
@LastModifiedBy: ywyz
@Github: https://github.com/ywyz
@LastEditors: ywyz
@LastEditTime: 2019-11-10 19:32:56
'''


def displaySortedNumbers(num1, num2, num3):
    if num1 > num2:
        num1, num2 = num2, num1
    if num2 > num3:
        num2, num3 = num3, num2
    if num1 > num2:
        num1, num2 = num2, num1

    return num1, num2, num3


def main():
    n1, n2, n3 = eval(input("Enter three number:"))
    print(displaySortedNumbers(n1, n2, n3))


main()
