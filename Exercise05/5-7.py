'''
@Date: 2019-09-04 20:17:23
@Author: ywyz
@LastModifiedBy: ywyz
@Github: https://github.com/ywyz
@LastEditors: ywyz
@LastEditTime: 2019-11-10 00:06:07
'''
import math
print("------------------------------ ------------------------------")
print(
    "        degree    |              sin                |          cos        "
)
degrees = 0
while degrees <= 360:
    if degrees <= 90 and degrees > 0:
        print("         ", degrees, "     |       ",
              format(math.sin(math.radians(degrees)), "15.4f"),
              "         |          ",
              format(math.cos(math.radians(degrees)), "15.4f"), "       ")
    elif degrees == 0:
        print("          ", degrees, "     |       ",
              format(math.sin(math.radians(degrees)), "15.4f"),
              "         |          ",
              format(math.cos(math.radians(degrees)), "15.4f"), "       ")
    else:
        print("        ", degrees, "     |       ",
              format(math.sin(math.radians(degrees)), "15.4f"),
              "         |          ",
              format(math.cos(math.radians(degrees)), "15.4f"), "       ")
    degrees += 10
