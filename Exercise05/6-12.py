'''
@Date: 2019-11-10 21:25:00
@Author: ywyz
@LastModifiedBy: ywyz
@Github: https://github.com/ywyz
@LastEditors: ywyz
@LastEditTime: 2019-11-10 21:32:08
'''


def main():
    printChars("1", "Z", 10)


def printChars(ch1, ch2, numberPerLine):
    number = ord(ch2) - ord(ch1)
    temp = 1
    for n in range(number + 1):
        print(ch1, end=" ")
        ch1 = chr(ord(ch1) + 1)
        if temp % 10 == 0:
            print("")
        temp += 1


main()
