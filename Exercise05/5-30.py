'''
@Date: 2019-11-02 09:19:19
@Author: ywyz
@LastModifiedBy: ywyz
@Github: https://github.com/ywyz
@LastEditors: ywyz
@LastEditTime: 2019-11-02 10:13:44
'''
year = eval(input("Enter the year: "))
day = eval(input("Enter the day of the week: "))

for months in range(1, 13):
    if months == 1:
        month = "January"
        dayOfMonths = 31
        firstday = day
    elif months == 2:
        month = "February"
        if (year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)):
            dayOfMonths = 29
        else:
            dayOfMonths = 28
    elif months == 3:
        month = "March"
        dayOfMonths = 31
    elif months == 4:
        month = "April"
        dayOfMonths = 30
    elif months == 5:
        month = "May"
        dayOfMonths = 31
    elif months == 6:
        month = "June"
        dayOfMonths = 30
    elif months == 7:
        month = "July"
        dayOfMonths = 31
    elif months == 8:
        month = "Augest"
        dayOfMonths = 31
    elif months == 9:
        month = "September"
        dayOfMonths = 30
    elif months == 10:
        month = "October"
        dayOfMonths = 31
    elif months == 11:
        month = "November"
        dayOfMonths = 30
    elif months == 12:
        month = "December"
        dayOfMonths = 31

    if firstday == 1:
        dayOfWeek = "Monday"
        print(month, " . 1", year, "is ", dayOfWeek)
    elif firstday == 2:
        dayOfWeek = "Tuesday"
        print(month, " . 1", year, "is ", dayOfWeek)
    elif firstday == 3:
        dayOfWeek = "Wednesday"
        print(month, " . 1", year, "is ", dayOfWeek)
    elif firstday == 4:
        dayOfWeek = "Thursday"
        print(month, " . 1", year, "is ", dayOfWeek)
    elif firstday == 5:
        dayOfWeek = "Friday"
        print(month, " . 1", year, "is ", dayOfWeek)
    elif firstday == 6:
        dayOfWeek = "Saturday"
        print(month, " . 1", year, "is ", dayOfWeek)
    elif firstday == 0:
        dayOfWeek = "Sunday"
        print(month, " . 1", year, "is ", dayOfWeek)

    firstday = (firstday + dayOfMonths) % 7
