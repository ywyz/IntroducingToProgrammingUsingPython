'''
@Date: 2019-07-10 18:08:04
@Author: ywyz
@LastModifiedBy: ywyz
@Github: https://github.com/ywyz
@LastEditors: ywyz
@LastEditTime: 2019-07-10 19:04:20
'''
numberOfYears = eval(input("Enter the number of years: "))
time = 365 * 24 * 60 * 60
population = time // 7 - time // 13 + time // 45
populationYears = 31203249869 + population * numberOfYears
print("The population in ", numberOfYears, " years is", populationYears)
