'''
@Date: 2019-11-25 20:46:42
@Author: ywyz
@LastModifiedBy: ywyz
@Github: https://github.com/ywyz
@LastEditors: ywyz
@LastEditTime: 2019-11-25 20:49:02
'''
from random import randint


def getRandomCharacter(ch1, ch2):
    return chr(randint(ord(ch1), ord(ch2)))


def main():
    temp = 1
    tempWord = 'A'
    for n in range(100):
        tempWord = getRandomCharacter('A', 'Z')
        print(tempWord, end=" ")

        if temp % 10 == 0:
            print()
        temp += 1


main()
