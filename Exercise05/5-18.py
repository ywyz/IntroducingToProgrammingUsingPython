'''
@Date: 2019-09-09 19:17:47
@Author: ywyz
@LastModifiedBy: ywyz
@Github: https://github.com/ywyz
@LastEditors: ywyz
@LastEditTime: 2019-09-09 19:17:47
'''
number = eval(input("Enter the number: "))
fNumber = 2
print(number, "can be decomposed into :")
while fNumber <= number:
    if number % fNumber == 0:
        number = number / fNumber
        print(fNumber, end=" ")
    else:
        fNumber += 1
