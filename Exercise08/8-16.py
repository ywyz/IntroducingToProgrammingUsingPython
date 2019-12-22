'''
@Date: 2019-12-22 20:38:38
@Author: ywyz
@LastModifiedBy: ywyz
@Github: https://github.com/ywyz
@LastEditors  : ywyz
@LastEditTime : 2019-12-22 20:52:02
'''
strings = input("Enter the first 12 digits of an ISBN-13 as a string: ")
temp = 1
total = 0
for i in strings:
    if temp % 2 == 0:
        total += 3 * int(i)
    else:
        total += int(i)
    temp += 1
    
total = 10 - total % 10
if total == 10:
    total = 0

strings = strings + str(total)

print("The ISBN-13 number is ", strings)
