'''
@Date: 2019-07-10 17:07:59
@Author: ywyz
@LastModifiedBy: ywyz
@Github: https://github.com/ywyz
@LastEditors: ywyz
@LastEditTime: 2019-07-10 17:10:44
'''
balance, interestrate = eval(
    input("Enter balance and interest rate(e.g., 3 for 3%:"))
interest = balance * (interestrate / 1200)
print("The interest is ", interest)
