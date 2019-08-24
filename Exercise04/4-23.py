'''
@Date: 2019-08-24 18:24:10
@Author: ywyz
@LastModifiedBy: ywyz
@Github: https://github.com/ywyz
@LastEditors: ywyz
@LastEditTime: 2019-08-24 18:24:52
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

if (tempx <= 5) and (y <= 2.5):
    print("point( ", x, " ,", y, " ) is in thr rectangle.")
else:
    print("point( ", x, " ,", y, ") is not in thr rectangle.")
