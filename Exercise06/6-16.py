'''
@Date: 2019-11-11 21:53:24
@Author: ywyz
@LastModifiedBy: ywyz
@Github: https://github.com/ywyz
@LastEditors: ywyz
@LastEditTime: 2019-11-11 21:57:22
'''


def numberOfDaysInAYear(year):
    isLeapYear = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
    if isLeapYear:
        return 366
    else:
        return 365


def main():
    for years in range(2010, 2021):
        print(years, " have ", numberOfDaysInAYear(years), " days.")


main()
