'''
@Date: 2019-12-22 19:37:21
@Author: ywyz
@LastModifiedBy: ywyz
@Github: https://github.com/ywyz
@LastEditors  : ywyz
@LastEditTime : 2019-12-22 19:40:33
'''


def reverse(s):
    reversedStings = ""
    for n in s:
        reversedStings = n + reversedStings

    return reversedStings


def main():
    strings = input("Enter a strings: ")
    print(reverse(strings))


main()
