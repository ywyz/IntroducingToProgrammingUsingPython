'''
@Date: 2019-09-07 09:23:41
@Author: ywyz
@LastModifiedBy: ywyz
@Github: https://github.com/ywyz
@LastEditors: ywyz
@LastEditTime: 2019-09-07 09:23:42
'''
n = 0
for number in range(100, 1000):
    if n != 10:
        if number % 5 == 0 or number % 6 == 0:
            if number % 5 == 0 and number % 6 == 0:
                number += 1
                continue
            else:
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
