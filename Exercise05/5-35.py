'''
@Date: 2019-11-06 19:34:16
@Author: ywyz
@LastModifiedBy: ywyz
@Github: https://github.com/ywyz
@LastEditors: ywyz
@LastEditTime: 2019-11-06 19:35:11
'''
for i in range(1, 10001):
    k = 0
    for j in range(1, i):
        if (i % j == 0):
            k += j

    if k == i:
        print(k)
