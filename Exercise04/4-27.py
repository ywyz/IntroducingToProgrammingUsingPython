'''
@Date: 2019-08-26 16:34:35
@Author: ywyz
@LastModifiedBy: ywyz
@Github: https://github.com/ywyz
@LastEditors: ywyz
@LastEditTime: 2019-08-26 16:34:35
'''
x, y = eval(input("Enter a point's x- and y-coordinates: "))
tempy = -0.5 * x + 100
if (tempy > y and y > 0 and x > 0):
    print("The point is in the triangle.")
else:
    print("The point is not in triangle.")
