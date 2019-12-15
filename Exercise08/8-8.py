'''
@Date: 2019-12-15 20:31:38
@Author: ywyz
@LastModifiedBy: ywyz
@Github: https://github.com/ywyz
@LastEditors: ywyz
@LastEditTime: 2019-12-15 20:38:11
'''


def binaryToDecimal(binaryString):
    length = len(binaryString) - 1
    total = 0

    for num in binaryString:
        total += (int(num) * 2**length)
        length -= 1

    return total


def main():
    binaryStings = input("Enter a binary strings: ")
    print(binaryToDecimal(binaryStings))


main()
