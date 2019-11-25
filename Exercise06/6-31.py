'''
@Date: 2019-11-25 19:25:05
@Author: ywyz
@LastModifiedBy: ywyz
@Github: https://github.com/ywyz
@LastEditors: ywyz
@LastEditTime: 2019-11-25 19:30:05
'''
from time import time


def isYeapYear(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False


def main():
    currentTime = time()

    # Obtain the total seconds since midnight, Jan 1, 1970
    totalSeconds = int(currentTime)

    # Get the current second
    currentSecond = totalSeconds % 60

    # Obtain the total minutes
    totalMInutes = totalSeconds // 60

    # Compute the current minute in the hour
    currentMinute = totalMInutes % 60

    # Obtain the total hours
    totalHours = totalMInutes // 60

    # Compute the current hour
    currentHour = totalHours % 24
    days = totalHours // 24

    year = 1970
    while days >= 365:
        if isYeapYear(year):
            days -= 366
        else:
            days -= 365

        year += 1

    month = 1
    while days > 31:
        if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
            days -= 31
            month += 1
            continue
        elif month == 2:
            if isYeapYear(year):
                days -= 29
                month += 1
                continue
            else:
                days -= 28
                month += 1
                continue
        else:
            days -= 30
            month += 1
            continue

    if (month == 4 or month == 6 or month == 9 or month == 11) and days == 31:
        days -= 30
        month += 1


# Display results
    print("Current time is", month, days + 1, year, currentHour, ":",
          currentMinute, ":", currentSecond, "GMT")

main()