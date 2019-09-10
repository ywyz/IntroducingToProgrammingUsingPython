'''
@Date: 2019-09-06 18:36:56
@Author: ywyz
@LastModifiedBy: ywyz
@Github: https://github.com/ywyz
@LastEditors: ywyz
@LastEditTime: 2019-09-09 19:18:10
'''
n = 0
for number in range(100, 1000):
    if n != 10:
        if number % 5 == 0 and number % 6 == 0:
            print(number, end=" ")
            n += 1
            number += 1
            continue
        else:
            number += 1
            continue
    else:
        print("\n", number, end=" ")
        number += 1
        n = 1
        continue
