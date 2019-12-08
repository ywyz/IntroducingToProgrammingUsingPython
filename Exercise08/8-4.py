'''
@Date: 2019-12-08 19:58:01
@Author: ywyz
@LastModifiedBy: ywyz
@Github: https://github.com/ywyz
@LastEditors: ywyz
@LastEditTime: 2019-12-08 20:01:19
'''


def count(s, ch):
    num = 0
    for char in s:
        if char == ch:
            num += 1

    return num


def main():
    strings = input("Input a string: ")
    ch = input("Enter a word: ")
    print(ch, "has ", count(strings, ch), "times appeared in the strings.")


main()
