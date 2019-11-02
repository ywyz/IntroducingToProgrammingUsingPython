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
    
    if firstday == 1                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      
