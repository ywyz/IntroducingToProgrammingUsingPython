'''
@Date: 2019-10-04 19:52:25
@Author: ywyz
@LastModifiedBy: ywyz
@Github: https://github.com/ywyz
@LastEditors: ywyz
@LastEditTime: 2019-10-04 20:00:37
'''
number1 = 0
number2 = 0
for n in range(1, 50001):
    number1 += 1 / n

n = 50000
while n > 0:
    number2 += 1 / n
    n -= 1

print(number1)
print(number2)
