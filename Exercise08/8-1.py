'''
@Date: 2019-12-07 19:41:45
@Author: ywyz
@LastModifiedBy: ywyz
@Github: https://github.com/ywyz
@LastEditors: ywyz
@LastEditTime: 2019-12-07 20:05:09
'''


def Test(line):
    if len(line) == 11:
        if line[:3].isdigit() and line[3] == "-" and line[4:6].isdigit(
        ) and line[6] == "-" and line[7:-1].isdigit():
            return True
    else:
        return False


def main():
    line = input("Enter SSN:")
    if Test(line):
        print("Vaild SSN")
    else:
        print("Invaid SSN")


main()
