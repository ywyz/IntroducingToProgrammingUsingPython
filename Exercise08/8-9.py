'''
@Date: 2019-12-20 21:22:42
@Author: ywyz
@LastModifiedBy: ywyz
@Github: https://github.com/ywyz
@LastEditors  : ywyz
@LastEditTime : 2019-12-22 18:37:59
'''


def binaryToHex(binaryValue):
    length = len(binaryValue)
    while length % 4 != 0:
        binaryValue = '0' + binaryValue
        length = len(binaryValue)
    startLength = 0
    endLength = startLength + 4
    while endLength <= length:
        temp = binaryValue[startLength:endLength]
        numTemp = 3
        total = 0
        while numTemp >= 0:
            total += int(temp[3 - numTemp]) * 2**numTemp
            numTemp -= 1

        if total == 10:
            print('A', end="")

        elif total == 11:
            print('B', end="")

        elif total == 12:
            print('C', end="")

        elif total == 13:
            print('D', end="")

        elif total == 14:
            print('E', end="")

        elif total == 15:
            print('F', end="")

        else:
            print(total, end="")

        startLength += 4
        endLength += 4


def main():
    strings = input("Enter a binary strings: ")
    binaryToHex(strings)
    print()


main()
