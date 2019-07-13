'''
@Date: 2019-06-29 18:18:47
@Author: ywyz
@LastModifiedBy: ywyz
@Github: https://github.com/ywyz
@LastEditors: ywyz
@LastEditTime: 2019-07-04 16:18:09
'''
amountWater = eval(input("Enter the amount of water in kilograms: "))
intialTemperature = eval(input("Enter the intial temperature: "))
finalTemperature = eval(input("Enter the final temperature:"))
needEnergy = amountWater * (finalTemperature - intialTemperature) * 4184
print("The energy needed is", needEnergy)
