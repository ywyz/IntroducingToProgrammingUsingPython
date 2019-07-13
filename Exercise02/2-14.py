'''
@Date: 2019-07-04 19:40:13
@Author: ywyz
@LastModifiedBy: ywyz
@Github: https://github.com/ywyz
@LastEditors: ywyz
@LastEditTime: 2019-07-05 09:33:44
'''
x1, y1, x2, y2, x3, y3 = eval(input("Enter three points for a triangle: "))
side1 = ((x2 - x1)**2 + (y2 - y1)**2)**0.5  # 左
side2 = ((x3 - x1)**2 + (y3 - y1)**2)**0.5  # 下
side3 = ((x3 - x2)**2 + (y3 - y2)**2)**0.5  # 右
s = (side1 + side2 + side3) / 2
area = (s * (s - side1) * (s - side2) * (s - side3))
print("The area of the triangle is ", 33.6)
