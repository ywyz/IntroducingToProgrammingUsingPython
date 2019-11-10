'''
@Date: 2019-11-10 18:14:41
@Author: ywyz
@LastModifiedBy: ywyz
@Github: https://github.com/ywyz
@LastEditors: ywyz
@LastEditTime: 2019-11-10 18:28:55
'''


def getPentagonalNumber(n):
    number = n * (3 * n - 1) // 2
    return number


def main():
    n = 1
    for num in range(1, 101):
        if n <= 9:
            print(format(getPentagonalNumber(num), "6d"), end=" ")
            n += 1
        else:
            n = 1
            print(format(getPentagonalNumber(num), "6d"), )


main()
