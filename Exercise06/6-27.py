'''
@Date: 2019-11-17 15:02:44
@Author: ywyz
@LastModifiedBy: ywyz
@Github: https://github.com/ywyz
@LastEditors: ywyz
@LastEditTime: 2019-11-17 15:04:22
'''


def isPrimeNumber(n):
    for temp in range(2, n):
        if n % temp == 0:
            return False

    return True


def doublePrimeNumber(n1, n2):
    if n2 - n1 == 2:
        print("(", n1, ",", n2, ")")


def main():
    oldPrime = 2
    for n in range(2, 1001):
        if isPrimeNumber(n):
            newPrime = n
            doublePrimeNumber(oldPrime, newPrime)
            oldPrime = newPrime


main()
