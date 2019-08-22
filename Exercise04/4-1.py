'''
@Date: 2019-08-22 11:45:57
@Author: ywyz
@LastModifiedBy: ywyz
@Github: https://github.com/ywyz
@LastEditors: ywyz
@LastEditTime: 2019-08-22 11:52:12
'''
import math

a, b, c = eval(input("Enter a, b, c: "))

if (b**2 - 4 * a * c) < 0:
    print("The equction has no real roots.")

elif (b**2 - 4 * a * c) == 0:
    result = (-b + math.sqrt(b**2 - 4 * a * c)) / 2 * a
    print("The root is ", result)

else:
    result1 = (-b + math.sqrt(b**2 - 4 * a * c)) / 2 * a
    result2 = (-b - math.sqrt(b**2 - 4 * a * c)) / 2 * a
    print("The roots are ", result1, "and", result2)
