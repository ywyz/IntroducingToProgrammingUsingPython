'''
@Date: 2019-08-26 20:10:58
@Author: ywyz
@LastModifiedBy: ywyz
@Github: https://github.com/ywyz
@LastEditors: ywyz
@LastEditTime: 2019-08-26 20:11:34
'''
number = eval(input("Enter a decimal value (0 to 15): "))

if number >= 0 and number <= 9:
    print("The hex value is ", number)
elif number > 9 and number <= 15:
    print("The hex value is ", chr(ord("A") + number - 9 - 1))
else:
    print("Invaild input")
