'''
@Date: 2019-08-24 20:47:16
@Author: ywyz
@LastModifiedBy: ywyz
@Github: https://github.com/ywyz
@LastEditors: ywyz
@LastEditTime: 2019-08-24 20:47:16
'''
x1, y1, x2, y2, x3, y3, x4, y4 = eval(input("Enter x1,y1,x2,y2,x3,y3,x4,y4: "))

a = y1 - y2
b = -1 * (x1 - x2)
c = y3 - y4
d = -1 * (x3 - x4)
e = (y1 - y2) * x1 - (x1 - x2) * y1
f = (y3 - y4) * x3 - (x3 - x4) * y3

if (a * d - b * c) == 0:
    print("The two lines are parallel.")

else:
    finalX = (e * d - b * f) / (a * d - b * c)
    finalY = (a * f - e * c) / (a * d - b * c)
    print("The intersecting point is at (", finalX, ",", finalY, ")")
