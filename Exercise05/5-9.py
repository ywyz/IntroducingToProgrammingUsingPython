'''
@Date: 2019-09-05 18:40:02
@Author: ywyz
@LastModifiedBy: ywyz
@Github: https://github.com/ywyz
@LastEditors: ywyz
@LastEditTime: 2019-09-05 19:03:17
'''
year = 1
coat = 10000

while year <= 10:
    coat *= 1.05
    year += 1

print("Ten years coat is ", coat)

total = coat

for i in range(0, 3):
    coat *= 1.05
    total += coat

print("Ten years later the four years coat is ", total)
