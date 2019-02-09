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

# Display results
print("Current time is", currentHour, ":", currentMinute, ":", currentSecond,
      "GMT")
