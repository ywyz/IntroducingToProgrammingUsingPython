'''
@Date: 2019-11-13 06:29:39
@Author: ywyz
@LastModifiedBy: ywyz
@Github: https://github.com/ywyz
@LastEditors: ywyz
@LastEditTime: 2019-11-14 00:48:26
'''


def isPrimeNumber(n):
    for temp in range(2, n):
        if n % temp == 0:
            return False
    return True


def isTractNumber(n):
    if isPrimeNumber(n):
        oldnumber = n
        line = ""
        while n > 9:
            temp = n % 10
            line += str(temp)
            n //= 10
        line += str(n)
        if line == str(oldnumber):
            return False
        else:
            return isPrimeNumber(eval(line))
    else:
        return False


def main():
    n = 0
    number = 2
    while n < 100:
        if isTractNumber(number):
            print(format(number, "6d"), end=" ")
            n += 1
            if n % 10 == 0:
                print()
            number += 1
        else:
            number += 1


main()
