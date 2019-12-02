'''
@Date: 2019-12-02 20:59:38
@Author: ywyz
@LastModifiedBy: ywyz
@Github: https://github.com/ywyz
@LastEditors: ywyz
@LastEditTime: 2019-12-02 21:34:50
'''


class Account:
    def __init__(self, id=0, balance=100.0, annualInterestRate=0.0):
        self.__id = id
        self.__balance = balance
        self.__annualInterestRate = annualInterestRate

    def getId(self):
        return self.__id

    def setId(self, id):
        self.__id = id

    def getBalance(self):
        return self.__balance

    def setBalance(self, balance):
        self.__balance = balance

    def getAnnualInterestRate(self):
        return self.__annualInterestRate

    def setAnnualInterestRate(self, annualInterestRate):
        self.__annualInterestRate = annualInterestRate / 100

    def getMonthlyInterestRate(self):
        self.monthlyInterestRate = self.__annualInterestRate / 12 / 100
        return self.monthlyInterestRate

    def getMonthlyInterest(self):
        self.monthlyInterest = self.__balance * self.monthlyInterestRate
        return self.monthlyInterest

    def withDraw(self, money):
        self.__balance -= money

    def deposit(self, money):
        self.__balance += money


def main():
    account = Account(1122, 20000, 4.5)
    account.withDraw(2500)
    account.deposit(3000)
    print("Id: ", account.getId())
    print("Balance: ", account.getBalance())
    print("MonthlyInterestRate:",
          format(account.getMonthlyInterestRate(), ".1f"), "%")
    print("MonthlyInterest: ", format(account.getMonthlyInterest(), ".2f"))


main()
