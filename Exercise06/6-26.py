def primeNumber(n):
    for temp in range(2, n):
        if n % temp == 0:
            return False

    return True


def mersennePrimeNumber(n):
    prime = 2**n - 1
    if primeNumber(prime):
        return prime
    else:
        return False


def main():
    print("  p       2^p-1")
    for p in range(2, 32):
        if mersennePrimeNumber(p):
            print(format(p, "3d"), format(mersennePrimeNumber(p), "9d"))


main()
