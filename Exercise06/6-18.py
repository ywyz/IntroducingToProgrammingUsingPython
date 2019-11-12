from random import randint

def main():
    number = eval(input("Enter n: "))
    printMatrix(number)


def printMatrix(n):
    for line in range(n):
        for row in range(n):
            print(randint(0,1), end=" ")
        print("")

main()
