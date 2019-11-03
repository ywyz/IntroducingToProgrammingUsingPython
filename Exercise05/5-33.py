'''
@Date: 2019-11-03 15:05:23
@Author: ywyz
@LastModifiedBy: ywyz
@Github: https://github.com/ywyz
@LastEditors: ywyz
@LastEditTime: 2019-11-03 17:11:34
'''
initialDepositAmount = eval(input("Enter the initial deposit amount: "))
annualPercentageYield = eval(input("Enter annual percentage yield: "))
numberOfMonths = eval(input("Enter maturity period(number of months): "))
cdValue = initialDepositAmount + initialDepositAmount * (
    annualPercentageYield / 1200)
print("Month            CD Value")
for n in range(1, numberOfMonths + 1):
    print(n, "      ", cdValue)
    cdValue = cdValue + cdValue * (annualPercentageYield / 1200)
