'''
@Date: 2019-07-04 17:10:16
@Author: ywyz
@LastModifiedBy: ywyz
@Github: https://github.com/ywyz
@LastEditors: ywyz
@LastEditTime: 2019-07-04 19:07:44
'''
finalAccountValue = eval(input("Enter final account value: "))
annualInteresetRate = eval(input("Enter annual interset rate in percent: "))
numberOfYears = eval(input("Enter number of years: "))
initialDeposit = finalAccountValue / (1 + annualInteresetRate / 12 / 100)**(
    numberOfYears * 12)

print("Initial deposit value is ", initialDeposit)
