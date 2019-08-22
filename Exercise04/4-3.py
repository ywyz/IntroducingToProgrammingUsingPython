'''
@Date: 2019-08-22 12:19:12
@Author: ywyz
@LastModifiedBy: ywyz
@Github: https://github.com/ywyz
@LastEditors: ywyz
@LastEditTime: 2019-08-22 12:37:11
'''
a, b, c, d, e, f = eval(input("Enter a, b, c, d, e, f: "))
if (a * d - b * c) == 0:
    print("The eqution has no solution.")

else:
    x = (e * d - b * f) / (a * d - b * c)
    y = (a * f - e * c) / (a * d - b * c)
    print("x is", format(x, "0.2f"), " and y is ", y)
