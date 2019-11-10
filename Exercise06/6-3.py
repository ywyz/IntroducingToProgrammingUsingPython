'''
@Date: 2019-11-10 18:42:14
@Author: ywyz
@LastModifiedBy: ywyz
@Github: https://github.com/ywyz
@LastEditors: ywyz
@LastEditTime: 2019-11-10 19:08:16
'''


def reserve(n):
    line = " "
    while n >= 10:
        number = n % 10
        n //= 10
        line += str(number)
    line += str(n)
    return eval(line)


def isPalindrome(number):
    return number == reserve(number)


def main():
    number = eval(input("Enter a number: "))
    if isPalindrome(number):
        print(number, " is palindrome.")
    else:
        print(number, " is not a palindrome.")


main()
