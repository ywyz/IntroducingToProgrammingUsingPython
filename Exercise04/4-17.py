'''
@Date: 2019-08-23 17:04:55
@Author: ywyz
@LastModifiedBy: ywyz
@Github: https://github.com/ywyz
@LastEditors: ywyz
@LastEditTime: 2019-08-23 17:24:49
'''
import random
import sys

number = random.randint(0, 2)
guess = eval(input("scissor (0), rock (1), paper(2): "))

if number == 0:
    computer = "scissor"
elif number == 1:
    computer = "rock"
else:
    computer = "paper"

if guess == 0:
    you = "scissor"
elif guess == 1:
    you = "rock"
elif guess == 2:
    you = "paper"
else:
    print("Input Wrong!")
    sys.exit()

if (number == 0 and guess == 1) or (number == 1
                                    and guess == 2) or (number == 2
                                                        and guess == 0):
    print("The computer is ", computer, ". You are ", you, "You won!")
elif number == guess:
    print("The computer is ", computer, ". You are ", you,
          " too. It is a draw!")
else:
    print("The computer is ", computer, ". You are ", you, "You lose!")
