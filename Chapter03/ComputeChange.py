'''
@Date: 2019-08-17 13:08:50
@Author: ywyz
@LastModifiedBy: ywyz
@Github: https://github.com/ywyz
@LastEditors: ywyz
@LastEditTime: 2019-08-17 13:08:51
'''
amount = eval(input("Enter an amount, for example, 11.56: "))

remainingAmount = int(amount * 100)

numberOfOneDollars = remainingAmount // 100
remainingAmount = remainingAmount % 100

numberOfQuarters = remainingAmount // 25
remainingAmount = remainingAmount % 25

numberOfDimes = remainingAmount // 10
remainingAmount = remainingAmount % 10

numberOfNickels = remainingAmount // 5
remainingAmount = remainingAmount % 5

numberOfPennies = remainingAmount

print("Your amount", amount, "Consists of\n", "\t", numberOfOneDollars,
      "dollars\n", "\t", numberOfQuarters, "quarters\n", "\t", numberOfDimes,
      "dimes\n", "\t", numberOfNickels, "nickels\n", "\t", numberOfPennies,
      "pennies")
