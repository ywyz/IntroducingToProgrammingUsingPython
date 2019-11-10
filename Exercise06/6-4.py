'''
@Date: 2019-11-10 19:09:57
@Author: ywyz
@LastModifiedBy: ywyz
@Github: https://github.com/ywyz
@LastEditors: ywyz
@LastEditTime: 2019-11-10 19:11:44
'''


def reserve(n):
    line = " "
    while n >= 10:
        number = n % 10
        n //= 10
        line += str(number)
    line += str(n)
    return eval(line)


def main():
    number = eval(input("Enter a number: "))
    print(reserve(number))


main()
