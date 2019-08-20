'''
@Date: 2019-08-19 18:02:03
@Author: ywyz
@LastModifiedBy: ywyz
@Github: https://github.com/ywyz
@LastEditors: ywyz
@LastEditTime: 2019-08-19 20:21:56
'''
remainingAmount = eval(input("Enter an amount, for example, 1156: "))

numberOfOneDollars = remainingAmount // 100
remainingAmount = remainingAmount % 100

numberOfQuarters = remainingAmount // 25
remainingAmount = remainingAmount % 25

numberOfDimes = remainingAmount // 10
remainingAmount = remainingAmount % 10

numberOfNickels = remainingAmount // 5
remainingAmount = remainingAmount % 5

numberOfPennies = remainingAmount

print("Your amount", remainingAmount, "Consists of\n", "\t",
      numberOfOneDollars, "dollars\n", "\t", numberOfQuarters, "quarters\n",
      "\t", numberOfDimes, "dimes\n", "\t", numberOfNickels, "nickels\n", "\t",
      numberOfPennies, "pennies")
