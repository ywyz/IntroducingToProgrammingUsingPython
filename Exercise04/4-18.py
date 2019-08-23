'''
@Date: 2019-08-23 18:53:51
@Author: ywyz
@LastModifiedBy: ywyz
@Github: https://github.com/ywyz
@LastEditors: ywyz
@LastEditTime: 2019-08-23 18:59:10
'''
exchangeRate = eval(input("Enter the exchange rate from dollar to RMB: "))
isChange = eval(input("Enter 0 to convert dollars to RMB and 1 vice versa: "))

if isChange == 1:
    RMBAmount = eval(input("Enter the RMB amount: "))
    dollar = RMBAmount / exchangeRate
    print("￥", RMBAmount, "is $", dollar)
elif isChange == 0:
    dollar = eval(input("Enter the dollar amount: "))
    RMBAmount = dollar * exchangeRate
    print("$", dollar, "is ￥", RMBAmount)
else:
    print("Incorrect input")
