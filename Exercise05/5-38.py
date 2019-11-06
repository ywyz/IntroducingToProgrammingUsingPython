'''
@Date: 2019-11-06 19:58:39
@Author: ywyz
@LastModifiedBy: ywyz
@Github: https://github.com/ywyz
@LastEditors: ywyz
@LastEditTime: 2019-11-06 20:38:37
'''
import time

seconds = eval(input("Enter the number of seconds: "))
number = seconds
for n in range(0, seconds):
    print(number, "seconds remaining.")
    time.sleep(1)
    number -= 1
print("Stopped")
