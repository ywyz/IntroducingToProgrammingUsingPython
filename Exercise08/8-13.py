'''
@Date: 2019-12-22 20:15:03
@Author: ywyz
@LastModifiedBy: ywyz
@Github: https://github.com/ywyz
@LastEditors  : ywyz
@LastEditTime : 2019-12-22 20:21:34
'''


def prefix(s1, s2):
    length1 = len(s1)
    length2 = len(s2)
    lenth = length2 if length1 > length2 else length1
    temp = ""
    for i in range(lenth):
        if s1[i] == s2[i]:
            temp += s1[i]

    return temp


def main():
    s1 = input("Input the first strings: ")
    s2 = input("Input the second strings: ")

    print(prefix(s1, s2))


main()
