'''
@Date: 2019-12-20 21:22:42
@Author: ywyz
@LastModifiedBy: ywyz
@Github: https://github.com/ywyz
@LastEditors: ywyz
@LastEditTime: 2019-12-22 05:25:13
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
            total += int(temp[numTemp]) * 2**numTemp
            numTemp -= 1

        if total == 10:
            print('A',ends="")

        elif total == 11:
            print('B',ends="")

        elif total == 12:
            print('C'ends="")

        elif total == 13:
            print('D',ends="")

        elif total == 14:
            print('E',ends="")

        elif total == 15:
            print('F',ends="")

        else:
            print(total,ends="")
        
        startLength += 4
        endLength += 4


def main():
    strings = input("Enter a binary strings: ")
    binaryToHex(strings)

main()
