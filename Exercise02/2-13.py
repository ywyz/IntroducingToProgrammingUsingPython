'''
@Date: 2019-07-04 19:14:58
@Author: ywyz
@LastModifiedBy: ywyz
@Github: https://github.com/ywyz
@LastEditors: ywyz
@LastEditTime: 2019-07-04 19:35:47
'''
integer = eval(input("Enter an integer: "))
lNumber = integer % 10  # 个位数
sNumber = (integer - lNumber) // 10 % 10  # 十位数
tNumber = (integer - sNumber * 10 - lNumber) // 100 % 10  # 百位数
fNumber = (integer - tNumber * 100 - sNumber * 10 -
           lNumber) // 1000 % 10  # 千位数
print(lNumber)
print(sNumber)
print(tNumber)
print(fNumber)
