'''
@Date: 2019-07-10 17:12:59
@Author: ywyz
@LastModifiedBy: ywyz
@Github: https://github.com/ywyz
@LastEditors: ywyz
@LastEditTime: 2019-07-10 18:05:17
'''
monthlySavingAmount = eval(input("Enter the monthly saving amount: "))
firstMonth = monthlySavingAmount * (1 + 0.00417)
secondMonth = (firstMonth + monthlySavingAmount) * (1 + 0.00417)
thirdMonth = (secondMonth + monthlySavingAmount) * (1 + 0.00417)
fourthMonth = (thirdMonth + monthlySavingAmount) * (1 + 0.00417)
fifthMonth = (fourthMonth + monthlySavingAmount) * (1 + 0.00417)
sixthMonth = (fifthMonth + monthlySavingAmount) * (1 + 0.00417)
print("After the sixth month, the account value is ", sixthMonth)
