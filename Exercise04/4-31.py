'''
@Date: 2019-08-26 19:41:26
@Author: ywyz
@LastModifiedBy: ywyz
@Github: https://github.com/ywyz
@LastEditors: ywyz
@LastEditTime: 2019-08-26 20:27:32
'''
x0, y0, x1, y1, x2, y2 = eval(
    input("enter coordinates for the three points p0, p1 and p2: "))

result = (x1 - x0) * (y2 - y0) - (x2 - x0) * (y1 - y0)

if result > 0:
    print("p2 is on the left side of the line from p0 to p1")
elif result == 0:
    print("p2 is on the same line from p0 to p1")
else:
    print("p2 is on the right side of the line from p0 to p1")
