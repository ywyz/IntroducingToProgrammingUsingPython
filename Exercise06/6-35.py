'''
@Date: 2019-11-25 20:30:44
@Author: ywyz
@LastModifiedBy: ywyz
@Github: https://github.com/ywyz
@LastEditors: ywyz
@LastEditTime: 2019-11-25 20:40:55
'''
from random import randint


def getRandomCharacter(ch1, ch2):
    return chr(randint(ord(ch1), ord(ch2)))


def main():
    temp = 1
    aNumber = 0
    tempWord = 'A'
    for n in range(10000):
        tempWord = getRandomCharacter('A', 'Z')
        print(tempWord, end=" ")
        temp += 1
        if tempWord == 'A':
            aNumber += 1
        if temp % 20 == 0:
            print()
        temp += 1
    print("The number of A is ", aNumber)


main()
