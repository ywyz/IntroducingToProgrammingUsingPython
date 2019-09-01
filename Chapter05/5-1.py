'''
@Date: 2019-09-01 18:47:02
@Author: ywyz
@LastModifiedBy: ywyz
@Github: https://github.com/ywyz
@LastEditors: ywyz
@LastEditTime: 2019-09-01 20:28:18
'''
number = eval(input("Enter an integer, the input ends if it is 0: "))

positiveNumber = 0
negativesNumber = 0
count = 0
totalnumber = 0
if number != 0:
    while number != 0:
        if number > 0:
            positiveNumber += 1
            count += 1
            totalnumber += number
            number = eval(
                input("Enter an integer, the input ends if it is 0: "))
            continue
        else:
            negativesNumber += 1
            count += 1
            totalnumber += number
            number = eval(
                input("Enter an integer, the input ends if it is 0: "))
            continue

    average = totalnumber / count

    print("The number of positives is ", positiveNumber)
    print("The number of negatives is ", negativesNumber)
    print("The total is ", totalnumber)
    print("The average is ", average)

else:
    print("You didn't enter any number.")
