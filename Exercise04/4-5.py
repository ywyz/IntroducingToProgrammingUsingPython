'''
@Date: 2019-08-22 15:52:40
@Author: ywyz
@LastModifiedBy: ywyz
@Github: https://github.com/ywyz
@LastEditors: ywyz
@LastEditTime: 2019-08-22 16:08:34
'''
TodayDay = eval(input("Enter today's day: "))
DaysElapsed = eval(input("Enter the number of days elapsed since today: "))
TotalDay = TodayDay + DaysElapsed

temp = TodayDay
if temp == 0:
    Today = "Sunday"
elif temp == 1:
    Today = "Monday"
elif temp == 2:
    Today = "Tuesday"
elif TodayDay == 3:
    Today = "Wednesday"
elif TodayDay == 4:
    Today = "Thursday"
elif TodayDay == 5:
    Today = "Friday"
elif TodayDay == 6:
    Today = "Sunday"
else:
    print("Wrong Input!")

temp = TotalDay % 7
if temp == 0:
    FutureDay = "Sunday"
elif temp == 1:
    FutureDay = "Monday"
elif temp == 2:
    FutureDay = "Tuesday"
elif temp == 3:
    FutureDay = "Wednesday"
elif temp == 4:
    FutureDay = "Thursday"
elif temp == 5:
    FutureDay = "Friday"
else:
    FutureDay = "Sunday"

print("Today is " + Today + " and  the future day is " + FutureDay)
