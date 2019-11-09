'''
@Date: 2019-09-14 17:50:32
@LastEditors: ywyz
@LastEditTime: 2019-11-10 00:16:26
@Author: ywyz
@Description: Introduction to Programming Using Python
'''

lineNumber = 8
nowLine = 0
for nowLine in range(0, lineNumber):
    temp = nowLine
    # 打印空格
    for temp in range(0, lineNumber - nowLine):
        print("    ", end="")
    # 顺序打印
    for temp in range(0, nowLine + 1):
        number = 2**temp
        print(format(number, "4d"), end="")

    # 倒序打印
    for temp in range(nowLine - 1, -1, -1):
        number = 2**temp
        print(format(number, "4d"), end="")

    print("\n")
