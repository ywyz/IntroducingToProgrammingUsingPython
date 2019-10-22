import math

i = eval(input("Enter the number of i: "))
e = 1
item = 1
for item in range(1, i):
    number = 1
    total = 1

    for number in range(1, item + 1):
        total *= number
    
    e = e + (1 / total)

print(e)