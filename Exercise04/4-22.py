'''
@Date: 2019-08-24 11:15:59
@Author: ywyz
@LastModifiedBy: ywyz
@Github: https://github.com/ywyz
@LastEditors: ywyz
@LastEditTime: 2019-08-24 11:19:44
'''
x, y = eval(input("Enter a point with two coordinates: "))
if x < 0:
    tempx = -1 * x
else:
    tempx = x
if y < 0:
    tempy = -1 * y
else:
    tempy = y

if (tempx**2 + tempy**2)**0.5 <= 10:
    print("point( ", x, " ,", y, " ) is in thr circle.")
else:
    print("point( ", x, " ,", y, ") is not in thr circle.")
