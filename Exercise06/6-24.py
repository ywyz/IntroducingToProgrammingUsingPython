'''
@Date: 2019-11-13 00:55:45
@Author: ywyz
@LastModifiedBy: ywyz
@Github: https://github.com/ywyz
@LastEditors: ywyz
@LastEditTime: 2019-11-13 01:28:02
'''


def isPrimeNumber(n):
    for number in range(2, n):
        if n % number == 0:
            return False

    return True


def isTractsNumber(n):
    line = str(n)
    newline = ""
    while n > 9:
        temp = (n % 10)
        newline += str(temp)
        n //= 10
    newline += str(n)
    if line == newline:
        return True
    else:
        return False


def main():
    number = 0
    n = 2
    temp = 0
    while number < 100:
        if isPrimeNumber(n) and isTractsNumber(n):
            print(format(n, "6d"), end=" ")
            number += 1
            n += 1
            temp += 1
        else:
            n += 1

        if number % 10 == 0:
            print("")


main()
