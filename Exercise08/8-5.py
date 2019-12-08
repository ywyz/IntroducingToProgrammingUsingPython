def count(s1, s2):
    firstLen = len(s1)
    secondLen = len(s2)
    num = 0
    distance = firstLen - secondLen
    temp = 0
    while temp <= distance:
        if s2 == s1[temp:temp + secondLen]:
            num += 1

        temp += 1

    return num


def main():
    s1 = input("Input the first strings: ")
    s2 = input("Input the second strings: ")
    print(s2, "appeared ", count(s1, s2), " times in ", s1)


main()
