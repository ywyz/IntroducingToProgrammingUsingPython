n = 2001
number = 1
while n < 2101:
    if number % 10 == 0:
        print("\n")
        number += 1
    if n % 100 == 0:
        if n % 400 == 0:
            print(n, end=" ")
            n += 1
            number += 1
            continue
        else:
            n += 1
            continue
    else:
        if n % 4 == 0:
            print(n, end=" ")
            n += 1
            number += 1
            continue
        else:
            n += 1
            continue
