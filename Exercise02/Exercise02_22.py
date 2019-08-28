'''
@Date: 2019-07-13 19:22:24
@Author: ywyz
@LastModifiedBy: ywyz
@Github: https://github.com/ywyz
@LastEditors: ywyz
@LastEditTime: 2019-07-13 19:22:24
'''
# Input number of years
numberOfYears = eval(input("Enter the number of years: "))

# Compute population
population = 3120324986 + numberOfYears * 365 * 24 * 60 * 60 // 7 - \
    numberOfYears * 365 * 24 * 60 * 60 // 13 + numberOfYears * 365 * 24 * 60 * 60 // 45

# Display results
print("The population in", numberOfYears, "years is", population)
