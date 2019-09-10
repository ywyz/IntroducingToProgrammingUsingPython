'''
@Date: 2019-09-09 19:47:49
@Author: ywyz
@LastModifiedBy: ywyz
@Github: https://github.com/ywyz
@LastEditors: ywyz
@LastEditTime: 2019-09-10 19:55:54
'''
lineNumber = eval(input("Enter the lines of number: (between 1 and 15)"))
nowline = 1

for nowline in range(1, lineNumber + 1):
    spacenumber = lineNumber - nowline

    temp = spacenumber
    while temp >= 0:
        print(" ", end=" ")
        temp -= 1

    temp = nowline
    while temp > 0:
        print(temp, end=" ")
        temp -= 1

    temp = 2
    while temp <= nowline:
        print(temp, end=" ")
        temp += 1
    print("\n")
