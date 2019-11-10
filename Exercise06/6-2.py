'''
@Date: 2019-11-10 18:34:54
@Author: ywyz
@LastModifiedBy: ywyz
@Github: https://github.com/ywyz
@LastEditors: ywyz
@LastEditTime: 2019-11-10 18:38:18
'''


def sumDigits(n):
    total = 0
    while n >= 10:
        total += (n % 10)
        n //= 10
    total += n
    return total


def main():
    number = eval(input("Enter a number: "))
    print(sumDigits(number))


main()
