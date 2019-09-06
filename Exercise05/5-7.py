'''
@Date: 2019-09-04 20:17:23
@Author: ywyz
@LastModifiedBy: ywyz
@Github: https://github.com/ywyz
@LastEditors: ywyz
@LastEditTime: 2019-09-04 20:24:48
'''
import math
print("------------------------------ ------------------------------")
print("        degree     |       sin         |          cos        |")
degrees = 0
while degrees <= 360:
    print("        ", degrees, "     |       ",
          format(math.sin(math.radians(degrees)), "15.4f"),
          "         |          ",
          format(math.cos(math.radians(degrees)), "15.4f"), "       ")
    degrees += 10
