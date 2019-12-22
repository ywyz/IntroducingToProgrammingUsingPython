'''
@Date: 2019-12-22 18:39:03
@Author: ywyz
@LastModifiedBy: ywyz
@Github: https://github.com/ywyz
@LastEditors  : ywyz
@LastEditTime : 2019-12-22 19:26:52
'''


def decimalToBinary(value):
    answer = ""
    while value != 0:
        num = value % 2
        value = value // 2
        answer = str(num) + answer

    return answer


def main():
    number = eval(input("Enter a number:"))
    print(decimalToBinary(number))


main()
