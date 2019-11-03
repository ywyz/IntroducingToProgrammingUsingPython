'''
@Date: 2019-11-03 17:32:07
@Author: ywyz
@LastModifiedBy: ywyz
@Github: https://github.com/ywyz
@LastEditors: ywyz
@LastEditTime: 2019-11-03 17:35:41
'''
import random

# Generate a lottery
lotteryDigit1 = random.randint(0, 9)
lotteryDigit2 = random.randint(0, 9)
while lotteryDigit2 == lotteryDigit1:
    lotteryDigit2 = random.randint(0, 9)
lottery = lotteryDigit1 * 10 + lotteryDigit2

# Prompt the user to enter a guess
guess = eval(input("Enter your lottery pick (two digits): "))

# Get digits from lottery

# Get digits from guess
guessDigit1 = guess // 10
guessDigit2 = guess % 10

print("The lottery number is", lottery)

# Check the guess
if guess == lottery:
    print("Exact match: you win $10,000")
elif (guessDigit2 == lotteryDigit1 and guessDigit1 == lotteryDigit2):
    print("Match all digits: you win $3,000")
elif (guessDigit1 == lotteryDigit1 or guessDigit1 == lotteryDigit2
      or guessDigit2 == lotteryDigit1 or guessDigit2 == lotteryDigit2):
    print("Match one digit: you win $1,000")
else:
    print("Sorry, no match")
