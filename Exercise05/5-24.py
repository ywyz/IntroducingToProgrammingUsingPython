'''
@Date: 2019-10-04 19:28:27
@Author: ywyz
@LastModifiedBy: ywyz
@Github: https://github.com/ywyz
@LastEditors: ywyz
@LastEditTime: 2019-10-04 19:51:41
'''
loanAmount = eval(input("Loan Amount: "))
numberOfYears = eval(input("Number of Years: "))
annualInterest = eval(input("Annual Interest Rate: "))

monthlyInterest = annualInterest / (numberOfYears * 12 * 100)
monthlyPayment = loanAmount * monthlyInterest / (1 - pow(
    (1 / (1 + monthlyInterest)), (numberOfYears * 12)))

totalPayment = monthlyPayment * numberOfYears * 12

print("Monthly Payment: ", monthlyPayment)
print("Total Payment: ", totalPayment)
balance = loanAmount
month = numberOfYears * 12
print("Payment#            Interest             Principal          Balance")
for n in range(1, month + 1):
    interest = monthlyInterest * balance
    principal = monthlyPayment - interest
    balance = balance - principal
    print(
        n,
        "\t\t",
        format(interest, "15.2f"),
        "\t\t",
        format(principal, "15.2f"),
        "\t\t",
        format(balance, "15.2f"),
    )
