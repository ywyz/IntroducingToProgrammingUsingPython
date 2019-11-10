'''
@Date: 2019-11-10 19:33:03
@Author: ywyz
@LastModifiedBy: ywyz
@Github: https://github.com/ywyz
@LastEditors: ywyz
@LastEditTime: 2019-11-10 19:49:00
'''


def displayPattern(n):
    for line in range(1, n + 1):
        for space in range(n - line):
            print("   ", end=" ")
        temp = line
        for row in range(line):
            print(format(temp, "3d"), end=" ")
            temp -= 1
        print("")


def main():
    number = eval(input("Enter a number:"))
    displayPattern(number)


main()
