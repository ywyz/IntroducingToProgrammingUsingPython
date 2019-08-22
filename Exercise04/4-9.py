'''
@Date: 2019-08-22 20:02:07
@Author: ywyz
@LastModifiedBy: ywyz
@Github: https://github.com/ywyz
@LastEditors: ywyz
@LastEditTime: 2019-08-22 20:02:07
'''
weight1, price1 = eval(input("Enter weight and price for package 1: "))
weight2, price2 = eval(input("Enter weight and price for package 2: "))
h1 = price1 / weight1
h2 = price2 / weight2
if (h1 > h2):
    print("Package 2 has a better price.")

elif (h2 > h1):
    print("Package 1 has a better price.")

else:
    print("They have same price.")
