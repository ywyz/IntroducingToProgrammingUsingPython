import math
n = 3
pi = 1
i = eval(input("Enter the number of i:"))
for n in range(2, i):
    pi += (math.pow(-1, n + 1) / (2 * n - 1))

pi *= 4
print(pi)
