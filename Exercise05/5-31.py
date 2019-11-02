'''
@Date: 2019-11-02 10:28:29
@Author: ywyz
@LastModifiedBy: ywyz
@Github: https://github.com/ywyz
@LastEditors: ywyz
@LastEditTime: 2019-11-02 17:44:40
'''
year = eval(input("Enter the year: "))
day = eval(input("Enter the day of the week: "))

for months in range(1, 13):
    if months == 1:
        month = "January"
        dayOfMonths = 31
        firstday = day
        total = firstday
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

    print('{:>30}'.format(month), year)
    print(
        "-------------------------------------------------------------------")
    print('{:>10}'.format('Sun'), '{:>10}'.format('Mon'),
          '{:>10}'.format('Tue'), '{:>10}'.format('Wed'),
          '{:>10}'.format('Thu'), '{:>10}'.format('Fri'),
          '{:>10}'.format('Sat'))
    for number in range(0, 7):
        if firstday >= number:
            print('{:>9}'.format(''), end="   ")
            total += 1
            continue
    for n in range(1, dayOfMonths + 1):
        print('{:>10}'.format(n), end="    ")
        total += 1
        if total > 7:
            print("\n")
            total = 1

    firstday = (firstday + dayOfMonths) % 7
    total = 0
    print('\n')
