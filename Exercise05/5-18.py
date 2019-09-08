number = eval(input("Enter the number: "))
fNumber = 2
print(number, "can be decomposed into :")
while fNumber <= number:
    if number % fNumber == 0:
        number = number / fNumber
        print(fNumber, end=" ")
    else:
        fNumber += 1
