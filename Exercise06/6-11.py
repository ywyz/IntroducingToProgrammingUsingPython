'''
@Date: 2019-11-10 21:04:28
@Author: ywyz
@LastModifiedBy: ywyz
@Github: https://github.com/ywyz
@LastEditors: ywyz
@LastEditTime: 2019-11-10 21:24:09
'''


def main():
    print("-------------------------------")
    print("  Sales Amount |  Commission")
    print("-------------------------------")
    salesAmount = 10000
    for n in range(18):
        print(format(salesAmount, "10d"), "    |   ",
              format(computeCommission(salesAmount), "8.1f"))
        print("-------------------------------")
        salesAmount += 5000
    return


def computeCommission(salesAmount):
    return 5000 * 0.08 + 5000 * 0.1 + (salesAmount - 10000) * 0.12


main()
