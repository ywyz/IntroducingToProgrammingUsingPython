def isVaild(number):
    if getSize(number) and prefixMatched(number):
        total = sumOfDoubleEvenPlace(number) + sumOfOddPlace(number)
        if total % 10 == 0:
            return True

    return False


def sumOfDoubleEvenPlace(number):
    number = eval(number)
    total = 0
    temp = 1
    line = ""
    while number > 10:
        line += str(number % 10)
        number //= 10

    line += str(number)

    for n in line:
        if temp % 2 != 0:
            temp += 1
            continue

        nTemp = getDigit(int(n) * 2)
        total += nTemp
        temp += 1

    return total


def getDigit(number):
    if number < 10:
        return number

    else:
        temp = number % 10
        number //= 10
        number += temp

    return number


def sumOfOddPlace(number):
    number = eval(number)
    temp = 1
    total = 0
    line = ""
    while number > 10:
        line += str(number % 10)
        number //= 10

    line += str(number)

    if len(line) % 2 == 0:
        for n in line:
            if temp % 2 == 0:
                temp += 1
                continue

            total += int(n)
            temp += 1
    else:
        for n in line:
            if temp % 2 != 0:
                temp += 1
                continue

            total += int(n)
            temp += 1
    return total


def prefixMatched(number):
    number = eval(number)
    while number > 10:
        while number > 100:
            number //= 10
        if number == 37:
            return True

        number //= 10

    if number == 4 or number == 5 or number == 6:
        return True

    return False


def getSize(d):
    d = eval(d)
    n = 0
    while d > 10:
        d //= 10
        n += 1

    n += 1
    if n >= 13 and n <= 16:
        return True

    else:
        return False


def main():
    number = input("Enter a card number: ")
    if isVaild(number):
        print("The card number is vaild.")

    else:
        print("The card number is invaild.")


main()
