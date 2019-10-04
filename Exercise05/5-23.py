'''
@Date: 2019-09-16 20:36:33
@Author: ywyz
@LastModifiedBy: ywyz
@Github: https://github.com/ywyz
@LastEditors: ywyz
@LastEditTime: 2019-10-04 19:05:01
'''
loanAmount = eval(input("Loan Amount: "))
numberOfYear = eval(input("Number of Years: "))

print("Interest Rate          Monthly Payment         Total Payment      ")
interestRate = 5.0

while interestRate <= 8.0:

    monthlyInterestRate = interestRate / 1200

    monthlyPayment = loanAmount * monthlyInterestRate / (1 - pow(
        (1 / (1 + monthlyInterestRate)), (numberOfYear * 12)))

    totalPayment = monthlyPayment * numberOfYear * 12

    print(format(interestRate / 100, "10.3%"), format(monthlyPayment, "20.3f"),
          format(totalPayment, "25.3f"))
    interestRate += 0.125
