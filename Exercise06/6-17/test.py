'''
@Date: 2019-11-11 23:31:40
@Author: ywyz
@LastModifiedBy: ywyz
@Github: https://github.com/ywyz
@LastEditors: ywyz
@LastEditTime: 2019-11-11 23:35:05
'''
from MyTriangle import isVaild
length1, length2, length3 = eval(input("Enter three sides in double:"))

if isVaild(length1, length2, length3):
    print("The area of the triangle is ", isVaild(length1, length2, length3))

else:
    print("Input is invaild")
