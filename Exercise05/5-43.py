'''
@Date: 2019-11-09 18:53:33
@Author: ywyz
@LastModifiedBy: ywyz
@Github: https://github.com/ywyz
@LastEditors: ywyz
@LastEditTime: 2019-11-09 19:00:19
'''
total = 0
for number1 in range(1, 8):
    for number2 in range(number1 + 1, 8):
        print(number1, number2)
        total += 1

print("THe total number of all combinations is ", total)
