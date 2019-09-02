'''
@Date: 2019-09-02 19:35:18
@Author: ywyz
@LastModifiedBy: ywyz
@Github: https://github.com/ywyz
@LastEditors: ywyz
@LastEditTime: 2019-09-02 19:44:57
'''
import random
import time

correctCount = 0 # Count the number of correct answers
count = 0 # Count the number of questions
NUMBER_OF_QUESTIONS = 5 # Constant

startTime = time.time() # Get start time

while count < NUMBER_OF_QUESTIONS:
    # 1. Generate two random single-digit integers
    number1 = random.randint(1, 15)
    number2 = random.randint(1, 15)


    # 3. Prompt the student to answer "what is number1 - number2?"
    answer = eval(input("What is " + str(number1) + " + " +
        str(number2) + "? "))

    # 5. Grade the answer and display the result
    if number1 + number2 == answer:
        print("You are correct!")
        correctCount += 1
    else:
        print("Your answer is wrong.\n", number1, "+",
            number2, "should be", (number1 + number2))

    # Increase the count
    count += 1

endTime = time.time() # Get end time
testTime = int(endTime - startTime) # Get test time
print("Correct count is", correctCount, "out of",
    NUMBER_OF_QUESTIONS, "\nTest time is", testTime, "seconds")
