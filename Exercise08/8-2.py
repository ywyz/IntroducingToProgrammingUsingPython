'''
@Date: 2019-12-08 18:50:29
@Author: ywyz
@LastModifiedBy: ywyz
@Github: https://github.com/ywyz
@LastEditors: ywyz
@LastEditTime: 2019-12-08 19:14:17
'''


def testStrings(str1, str2):
    firstLen = len(str1)
    secondLen = len(str2)
    n = 0
    while n < firstLen:
        if n + firstLen > secondLen:
            return -1
        if str1 == str2[n:n + firstLen]:
            return n
        n += 1

    return -1


def main():
    str1 = input("Input the first strings: ")
    str2 = input("Input the second strings: ")
    if testStrings(str1, str2) != -1:
        print(str1, "is the a substring of ", str2)

    else:
        print(str1, "is not the a substring of ", str2)


main()
