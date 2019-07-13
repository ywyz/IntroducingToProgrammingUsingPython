'''
@Date: 2019-07-06 09:53:05
@Author: ywyz
@LastModifiedBy: ywyz
@Github: https://github.com/ywyz
@LastEditors: ywyz
@LastEditTime: 2019-07-10 17:07:18
'''
investmentAmount = eval(input("Enter investment amount: "))
annualInterestRate = eval(input("Enter annual interest rate: "))
numberOfYears = eval(input("Enter number of years: "))
accumulatedValue = investmentAmount * (1 + annualInterestRate / 12 / 100)**(
    numberOfYears * 12)
print("Accumulated value is ", accumulatedValue)
