'''
@Date: 2019-11-09 19:16:56
@Author: ywyz
@LastModifiedBy: ywyz
@Github: https://github.com/ywyz
@LastEditors: ywyz
@LastEditTime: 2019-11-09 19:27:20
'''
value = ""
number = eval(input("Enter a number (Decimal): "))
while number >= 16:
    n = number % 16
    if n == 10:
        n = "A"
    elif n == 11:
        n = "B"
    elif n == 12:
        n = "C"
    elif n == 13:
        n = "D"
    elif n == 14:
        n = "E"
    elif n == 15:
        n = "F"

    value = str(n) + value
    number //= 16

if number == 10:
    n = "A"
elif number == 11:
    n = "B"
elif number == 12:
    n = "C"
elif number == 13:
    n = "D"
elif number == 14:
    n = "E"
elif number == 15:
    n = "F"

value = str(number) + value
print(value)