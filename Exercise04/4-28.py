'''
@Date: 2019-08-26 17:02:09
@Author: ywyz
@LastModifiedBy: ywyz
@Github: https://github.com/ywyz
@LastEditors: ywyz
@LastEditTime: 2019-08-26 20:49:41
'''
import math

x1, y1, width1, height1 = eval(
    input("Enter r1's center x- and y-coordinates,width, and height: "))
x2, y2, width2, height2 = eval(
    input("Enter r2's center x- and y-coordinates,width, and height: "))

width = math.fabs(x2 - x1)
height = math.fabs(y2 - y1)

if (width > ((width1 + width2) / 2)):
    print("r2 does not overlap r1.")
elif ((width < ((width1 + width2) / 2)) and (width > math.fabs(
    (width1 - width2) / 2))):
    if height > ((height1 + height2) / 2):
        print("r2 does not overlap r1.")
    elif (height < ((height1 + height2) / 2)) and (height > math.fabs(
        (height1 - height2) / 2)):
        print("r2 overlap r1.")
    elif (height < math.fabs((height1 - height2) / 2)):
        print("r2 overlap r1.")
elif width >= math.fabs((width1 - width2) / 2):
    if height > ((height1 + height2) / 2):
        print("r2 does not overlap r1.")
    elif (height < ((height1 + height2) / 2)) and (height > math.fabs(
        (height1 - height2) / 2)):
        print("r2 overlap r1.")
    elif (height < math.fabs((height1 - height2) / 2)):
        print("r2 is inside r1.")
