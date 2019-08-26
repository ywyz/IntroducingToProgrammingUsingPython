'''
@Date: 2019-08-26 18:58:39
@Author: ywyz
@LastModifiedBy: ywyz
@Github: https://github.com/ywyz
@LastEditors: ywyz
@LastEditTime: 2019-08-26 19:08:22
'''
import time

currentTime = time.time()

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
timeZone = eval(input("Enter the time zone offset to GMT:"))
currentHour += timeZone
if currentHour > 12:
    print("Current time is", currentHour - 12, ":", currentMinute, ":",
          currentSecond, "PM")
else:
    # Display results
    print("Current time is", currentHour, ":", currentMinute, ":",
          currentSecond, "AM")
