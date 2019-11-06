'''
@Date: 2019-11-06 20:42:45
@Author: ywyz
@LastModifiedBy: ywyz
@Github: https://github.com/ywyz
@LastEditors: ywyz
@LastEditTime: 2019-11-06 20:54:38
'''
GET = 25000
ADDTIMES = 0.01
sales = 0
haveGot = 0
while haveGot <= GET:
    if sales > 10000:
        haveGot = 5000 * 0.08 + 5000 * 0.1 + (sales - 10000) * 0.12

    else:
        haveGot = 5000 * 0.8 + (sales - 5000) * 0.1

    sales += ADDTIMES

print(sales)
