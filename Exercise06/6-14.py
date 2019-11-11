'''
@Date: 2019-11-11 20:42:10
@Author: ywyz
@LastModifiedBy: ywyz
@Github: https://github.com/ywyz
@LastEditors: ywyz
@LastEditTime: 2019-11-11 21:05:12
'''
import math


def calcultationpi(number):
    total = 0
    for n in range(1, number + 1):
        total += (math.pow(-1, n + 1) / (2 * n - 1))
    return total * 4


def main():
    print("-------------------------------")
    print("      i       |     m(i)     ")
    print("-------------------------------")
    for n in range(1, 1001, 100):
        print(format(n, "7d"), "    |   ", format(calcultationpi(n), "6.4f"))
        print("-------------------------------")


main()
