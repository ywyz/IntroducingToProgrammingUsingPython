'''
@Date: 2019-12-08 19:13:48
@Author: ywyz
@LastModifiedBy: ywyz
@Github: https://github.com/ywyz
@LastEditors: ywyz
@LastEditTime: 2019-12-08 19:52:23
'''


def lenth(str1):
    if len(str1) >= 8:
        return True
    else:
        return False


def testWord(str1):
    if str1.isalnum():
        return True

    else:
        return False


def testNumber(str1):
    num = 0
    length = len(str1)
    for n in range(length):
        if str1[n].isdigit():
            num += 1

    if num >= 2:
        return True

    else:
        return False


def main():
    password = input("Input the password: ")
    if lenth(password) and testWord(password) and testNumber(password):
        print("vaild password.")
    else:
        print("invaild password.")

main()
