'''
@Date: 2019-11-13 00:32:23
@Author: ywyz
@LastModifiedBy: ywyz
@Github: https://github.com/ywyz
@LastEditors: ywyz
@LastEditTime: 2019-11-13 00:47:14
'''


def convertMillis(millis):
    seconds = millis // 1000
    currentSeconds = seconds % 60
    minutes = seconds // 60
    currentMinutes = minutes % 60
    hours = minutes // 60
    time = str(hours) + " : " + str(currentMinutes) + " : " + str(
        currentSeconds)

    return time


def main():
    times = eval(input("Enter millis:"))
    print(convertMillis(times))


main()
