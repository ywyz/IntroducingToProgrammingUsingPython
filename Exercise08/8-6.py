'''
@Date: 2019-12-08 20:45:28
@Author: ywyz
@LastModifiedBy: ywyz
@Github: https://github.com/ywyz
@LastEditors: ywyz
@LastEditTime: 2019-12-08 21:14:02
'''


def countLetters(s):
    num = 0
    for n in s:
        if n.isalpha():
            num += 1

    return num


def main():
    strings = input("Input a strings: ")
    print(strings, " has", countLetters(strings), " words.")


main()
