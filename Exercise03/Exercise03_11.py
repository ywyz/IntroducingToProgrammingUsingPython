number = eval(input("Enter an integer: "))

d1 = number % 10
number = number // 10

d2 = number % 10
number = number // 10

d3 = number % 10
number = number // 10

d4 = number % 10
number = number // 10

print("The reversed number is", d1, end = '')
print(d2, end = '')
print(d3, end = '')
print(d4, end = '')
