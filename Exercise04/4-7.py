'''
@Date: 2019-08-22 16:56:25
@Author: ywyz
@LastModifiedBy: ywyz
@Github: https://github.com/ywyz
@LastEditors: ywyz
@LastEditTime: 2019-08-22 16:58:11
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

if numberOfPennies > 1:
    pennies = "pennies\n"
else:
    pennies = "penny\n"

if numberOfNickels > 1:
    nickels = "nickels\n"
else:
    nickels = "nickel\n"

if numberOfDimes > 1:
    dimes = "dimes\n"
else:
    dimes = "dime\n"

if numberOfQuarters > 1:
    quarters = "quarters\n"
else:
    quarters = "quarter\n"

if numberOfOneDollars > 1:
    dollors = "dollors\n"
else:
    dollors = " dollor\n"

print("Your amount", amount, "Consists of\n", "\t", numberOfOneDollars,
      dollors, "\t", numberOfQuarters, quarters, "\t", numberOfDimes, dimes,
      "\t", numberOfNickels, nickels, "\t", numberOfPennies, pennies)
