'''
@Date: 2019-11-26 21:41:11
@Author: ywyz
@LastModifiedBy: ywyz
@Github: https://github.com/ywyz
@LastEditors: ywyz
@LastEditTime: 2019-11-26 21:48:39
'''


def format(number, width):
    n = str(number)
    if len(n) >= width:
        return n

    else:
        num = len(n)
        lenth = width - num
        for zero in range(lenth):
            n = '0' + n

    return n


def main():
    number = eval(input("Enter an interger: "))
    width = eval(input("Enter the width: "))
    print("The formatted number is ", format(number, width))


main()
