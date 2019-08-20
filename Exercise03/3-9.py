'''
@Date: 2019-08-19 19:43:11
@Author: ywyz
@LastModifiedBy: ywyz
@Github: https://github.com/ywyz
@LastEditors: ywyz
@LastEditTime: 2019-08-19 21:28:03
'''
employeeName = input("Enter employee's name: ")
numberOfHours = eval(input("Enter number of hours worked in a week: "))
hourlyPayRate = eval(input("Enter hourly pay rate: "))
federalTax = eval(input("Enter federal tax withholding rate: "))
stateTax = eval(input("Enter state tax withholding rate: "))

grossPay = numberOfHours * hourlyPayRate
federal = grossPay * federalTax
state = grossPay * stateTax
totalDecution = federal + state
netPay = grossPay - totalDecution

print("Employee Name: ", employeeName)
print("Enter number of hours worked in a week: ", numberOfHours)
print("Pay Rate: $", hourlyPayRate)
print("Gross Pay: $", grossPay)
print("Decutions: ")
print("     Federal Withholding (", format(federalTax, "0.1%"), "): $",
      federal)
print("     State Withholding (", format(stateTax, "0.1%"), "): $", state)
print("     Total Decuction: $", totalDecution)
print("Net Pay: $", netPay)
