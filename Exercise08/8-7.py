'''
@Date: 2019-12-10 19:27:34
@Author: ywyz
@LastModifiedBy: ywyz
@Github: https://github.com/ywyz
@LastEditors: ywyz
@LastEditTime: 2019-12-15 20:31:05
'''


def getNumber(uppercaseLetter):
    if (uppercaseLetter == 'a' or uppercaseLetter == 'b'
            or uppercaseLetter == "c" or uppercaseLetter == 'A'
            or uppercaseLetter == 'B' or uppercaseLetter == "C"):
        return 2

    elif (uppercaseLetter == 'd' or uppercaseLetter == 'e'
          or uppercaseLetter == "f" or uppercaseLetter == 'D'
          or uppercaseLetter == 'E' or uppercaseLetter == "F"):
        return 3

    elif (uppercaseLetter == 'G' or uppercaseLetter == 'H'
          or uppercaseLetter == "I" or uppercaseLetter == 'g'
          or uppercaseLetter == 'h' or uppercaseLetter == "i"):
        return 4

    elif (uppercaseLetter == 'j' or uppercaseLetter == 'k'
          or uppercaseLetter == "l" or uppercaseLetter == 'J'
          or uppercaseLetter == 'K' or uppercaseLetter == "L"):
        return 5

    elif (uppercaseLetter == 'm' or uppercaseLetter == 'n'
          or uppercaseLetter == "o" or uppercaseLetter == 'M'
          or uppercaseLetter == 'N' or uppercaseLetter == "O"):
        return 6

    elif (uppercaseLetter == 'p' or uppercaseLetter == 'q'
          or uppercaseLetter == "r" or uppercaseLetter == 's'
          or uppercaseLetter == 'P' or uppercaseLetter == "Q"
          or uppercaseLetter == "R" or uppercaseLetter == "S"):
        return 7

    elif (uppercaseLetter == 't' or uppercaseLetter == 'u'
          or uppercaseLetter == "v" or uppercaseLetter == 'T'
          or uppercaseLetter == 'U' or uppercaseLetter == "V"):
        return 8

    else:
        return 9


def main():
    strings = input("Enter a strings:")
    phoneNumber = ""
    for word in strings:
        if word.isdigit():
            phoneNumber += str(word)
        elif word.isalnum():
            phoneNumber += str(getNumber(word))
        elif word == '-':
            phoneNumber += word
        else:
            continue

    print(phoneNumber)


main()
