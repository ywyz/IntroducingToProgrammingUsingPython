'''
@Date: 2019-08-21 21:37:31
@Author: ywyz
@LastModifiedBy: ywyz
@Github: https://github.com/ywyz
@LastEditors: ywyz
@LastEditTime: 2019-08-21 21:37:33
'''
year = eval(input("Enter a year: "))

# Check if the year is a leap year
isLeapYear = (year % 4 == 0 and year % 100 != 0) or \
   (year % 400 == 0)

# Display the result
print(year, "is a leap year?", isLeapYear)
