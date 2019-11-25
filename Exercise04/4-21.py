'''
@Date: 2019-08-24 10:38:36
@Author: ywyz
@LastModifiedBy: ywyz
@Github: https://github.com/ywyz
@LastEditors: ywyz
@LastEditTime: 2019-11-25 20:15:32
'''
year = eval(input("Enter year: (e.g., 2008 )"))
month = eval(input("Enter month: 1-12: "))
day = eval(input("Enter the day of month: "))

if month == 1:
    month = 13
    year = year - 1
elif month == 2:
    month = 14
    year = year - 1

dayOfWeek = (day + (26 * (month + 1) // 10) + year % 100 + (year % 100 // 4) +
             (year // 100 // 4) + 5 * (year // 100)) % 7

if dayOfWeek == 0:
    print("Day of the week is Saturday.")
elif dayOfWeek == 1:
    print("Day of the week is Sunday.")
elif dayOfWeek == 2:
    print("Day of the week is Monday.")
elif dayOfWeek == 3:
    print("Day of the week is Tuesday.")
elif dayOfWeek == 4:
    print("Day of the week is Wednesday.")
elif dayOfWeek == 5:
    print("Day of the week is Thursday.")
elif dayOfWeek == 6:
    print("Day of the week is Friday.")
else:
    print("Wrong!")
