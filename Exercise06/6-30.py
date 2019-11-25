'''
@Date: 2019-11-25 19:04:04
@Author: ywyz
@LastModifiedBy: ywyz
@Github: https://github.com/ywyz
@LastEditors: ywyz
@LastEditTime: 2019-11-25 19:11:01
'''
from random import randint


def rolledNumber():
    n1 = randint(1, 6)
    n2 = randint(1, 6)
    return n1, n2


def sumTotal(n1, n2):
    total = n1 + n2
    if total == 2 or total == 3 or total == 12:
        print("You rolled ", n1, " + ", n2, " = ", total)
        print("You lose")
        return False

    elif total == 7 or total == 11:
        print("You rolled ", n1, " + ", n2, " = ", total)
        print("You win")
        return True
    else:
        print("You rolled ", n1, " + ", n2, " = ", total)
        print("Point is ", total)
        n1, n2 = rolledNumber()
        temp = n1 + n2
        while temp != 7 and temp != total:
            n1, n2 = rolledNumber()
            temp = n1 + n2
            print("You rolled ", n1, " + ", n2, " = ", temp)

        if (n1 + n2) == 7:
            print("You rolled ", n1, " + ", n2, " = ", n1 + n2)
            print("You lose")
            return False

        else:
            print("You rolled ", n1, " + ", n2, " = ", n1 + n2)
            print("You win")
            return True


def main():
    n1, n2 = rolledNumber()
    winNumber = 0
    loseNumber = 0
    for n in range(10000):
        if sumTotal(n1, n2):
            winNumber += 1
        else:
            loseNumber += 1
        n1, n2 = rolledNumber()

    print("The number of win: ", winNumber)
    print("The number of lose: ", loseNumber)


main()
