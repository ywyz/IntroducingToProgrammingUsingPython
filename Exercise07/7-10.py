'''
@Date: 2019-12-04 20:58:34
@Author: ywyz
@LastModifiedBy: ywyz
@Github: https://github.com/ywyz
@LastEditors: ywyz
@LastEditTime: 2019-12-04 21:24:46
'''
from time import time


class Time:
    def __init__(self):
        self.setTime(int(time()))

    def getHour(self):
        return self.__hour

    def getMinute(self):
        return self.__minute

    def getSecond(self):
        return self.__second

    def setTime(self, elapseTime):
        currentTime = elapseTime

        # Obtain the total seconds since midnight, Jan 1, 1970
        totalSeconds = int(currentTime)

        # Get the current second
        self.__second = totalSeconds % 60

        # Obtain the total minutes
        totalMInutes = totalSeconds // 60

        # Compute the current minute in the hour
        self.__minute = totalMInutes % 60

        # Obtain the total hours
        totalHours = totalMInutes // 60

        # Compute the current hour
        self.__hour = totalHours % 24


def main():
    t = Time()
    # Display results
    print("Current time is", t.getHour(), ":", t.getMinute(), ":",
          t.getSecond(), "GMT")

    elapseTime = eval(input("Enter the elapsed time:"))

    t.setTime(elapseTime)

    print("The hour:minute:second for the elapsef time is ", t.getHour(), ":",
          t.getMinute(), ":", t.getSecond())


main()
