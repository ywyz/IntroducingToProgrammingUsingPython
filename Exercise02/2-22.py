'''
@Date: 2019-07-10 18:08:04
@Author: ywyz
@LastModifiedBy: ywyz
@Github: https://github.com/ywyz
@LastEditors: ywyz
@LastEditTime: 2019-07-13 19:46:20
'''
numberOfYears = eval(input("Enter the number of years: "))
time = 365 * 24 * 60 * 60
population = 3120324986 + time // (7 - 13 + 45) * numberOfYears
print("The population in ", numberOfYears, " years is", population)
