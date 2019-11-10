'''
@Date: 2019-11-10 20:54:41
@Author: ywyz
@LastModifiedBy: ywyz
@Github: https://github.com/ywyz
@LastEditors: ywyz
@LastEditTime: 2019-11-10 21:00:51
'''


def isPrime(number):
    divisor = 2
    while divisor <= number / 2:
        if number % divisor == 0:
            # If true, number is not prime
            return False  # number is not a prime
        divisor += 1

    return True


def main():
    count = 0
    for n in range(2, 10000):
        if isPrime(n):
            count += 1

    print(count)


main()
