'''
@Date: 2019-11-24 22:20:08
@Author: ywyz
@LastModifiedBy: ywyz
@Github: https://github.com/ywyz
@LastEditors: ywyz
@LastEditTime: 2019-11-25 18:39:31
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
    elif total == 7 or total == 11:
        print("You rolled ", n1, " + ", n2, " = ", total)
        print("You win")
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

        else:
            print("You rolled ", n1, " + ", n2, " = ", n1 + n2)
            print("You win")


def main():
    n1, n2 = rolledNumber()
    sumTotal(n1, n2)


main()
