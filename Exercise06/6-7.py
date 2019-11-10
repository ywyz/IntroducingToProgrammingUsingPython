'''
@Date: 2019-11-10 19:56:39
@Author: ywyz
@LastModifiedBy: ywyz
@Github: https://github.com/ywyz
@LastEditors: ywyz
@LastEditTime: 2019-11-10 20:13:46
'''


def futureInvestmentValue(investAmount, monthlyInterestRate, years):
    total = investAmount * (1 + monthlyInterestRate)**(years * 12)
    return total


def main():
    amountInvest = eval(input("The amount invested: "))
    annualIntersetRate = eval(input("Annual interest rate: "))
    print("Years           Future Value")
    for year in range(1, 31):
        print(
            format(year, "<6d"),
            format(
                futureInvestmentValue(amountInvest, annualIntersetRate / 1200,
                                      year), "20.2f"))


main()
