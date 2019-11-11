'''
@Date: 2019-11-10 23:07:53
@Author: ywyz
@LastModifiedBy: ywyz
@Github: https://github.com/ywyz
@LastEditors: ywyz
@LastEditTime: 2019-11-10 23:19:37
'''


def calcultationSeries(number):
    total = 0
    for n in range(1, number + 1):
        total += (n / (n + 1))
    return total


def main():
    print("-------------------------------")
    print("      i       |     m(i)     ")
    print("-------------------------------")
    for n in range(1, 21):
        print(format(n, "7d"), "    |   ", format(calcultationSeries(n),
                                                  "6.1f"))
        print("-------------------------------")


main()
