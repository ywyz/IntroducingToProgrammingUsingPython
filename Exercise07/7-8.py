'''
@Date: 2019-12-04 19:32:51
@Author: ywyz
@LastModifiedBy: ywyz
@Github: https://github.com/ywyz
@LastEditors: ywyz
@LastEditTime: 2019-12-04 20:35:35
'''
from time import time


class StopWatch:
    def __init__(self, startTime=time()):
        self.__startTime = startTime
        self.__endTime = startTime

    def getStartTime(self):
        return self.__startTime

    def getEndTime(self):
        return self.__endTime

    def start(self):
        self.__startTime = time()

    def stop(self):
        self.__endTime = time()

    def getElapsedTime(self):
        return self.__endTime - self.__startTime


def main():
    watch = StopWatch()
    watch.start()
    for i in range(1, 1000000):
        continue
    watch.stop()
    print("The time of 1 to 1,000,000 is ", watch.getElapsedTime(), "ms.")


main()
