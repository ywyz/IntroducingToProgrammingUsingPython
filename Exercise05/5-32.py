'''
@Date: 2019-11-02 18:48:35
@Author: ywyz
@LastModifiedBy: ywyz
@Github: https://github.com/ywyz
@LastEditors: ywyz
@LastEditTime: 2019-11-03 14:55:14
'''
monthlySave = eval(input("Enter the monthly saved: "))
interestRate = eval(input("Enter the annual interest rate:"))
months = eval(input("Enter the number of months: "))
monthlyRate = interestRate / 1200
total = monthlySave * (1 + monthlyRate)
for monthly in range(0, months):
    total = (total + monthlySave) * (1 + monthlyRate)

print("After ", months, "months, the account value is ", total)
