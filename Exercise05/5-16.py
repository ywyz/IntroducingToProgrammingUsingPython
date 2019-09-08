'''
@Date: 2019-09-07 10:35:38
@Author: ywyz
@LastModifiedBy: ywyz
@Github: https://github.com/ywyz
@LastEditors: ywyz
@LastEditTime: 2019-09-07 11:17:26
'''
n1 = eval(input("Enter the number 1: "))
n2 = eval(input("Enter the number 2: "))
n = n1 if n2 > n1 else n2
while n >= 1:
    if n1 % n == 0 and n2 % n == 0:
        break
    else:
        n -= 1
print("The GCD of n1 and n2 is ", n)
