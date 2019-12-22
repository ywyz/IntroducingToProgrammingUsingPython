'''
@Date: 2019-12-22 20:33:28
@Author: ywyz
@LastModifiedBy: ywyz
@Github: https://github.com/ywyz
@LastEditors  : ywyz
@LastEditTime : 2019-12-22 20:38:20
'''
strings = input("Enter the first 9 digits of an ISBN-10 as a string: ")
temp = 1
total = 0
for i in strings:
    total += int(i) * temp
    temp += 1

total %= 11
if total == 10:
    strings += 'X'
else:
    strings += str(total)

print("The ISBN-10 number is ", strings)
