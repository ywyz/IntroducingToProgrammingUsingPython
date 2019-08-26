'''
@Date: 2019-08-26 18:20:52
@Author: ywyz
@LastModifiedBy: ywyz
@Github: https://github.com/ywyz
@LastEditors: ywyz
@LastEditTime: 2019-08-26 18:55:55
'''
import math

x1, y1, radius1 = eval(
    input("Enter circle1's center x-, y-coordinates,and radius: "))
x2, y2, radius2 = eval(
    input("Enter circle2's center x-, y-coordinates, and radius: "))
radius = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

if (radius >= math.fabs(radius1 + radius2)):
    print("circle2 does not overlap circle1")
elif ((radius < math.fabs(radius1 + radius2))
      and (radius > math.fabs(radius1 - radius2))):
    print("circle2 overlaps circle1")
else:
    print("circle2 is inside circle1")
