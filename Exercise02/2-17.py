'''
@Date: 2019-07-05 16:00:18
@Author: ywyz
@LastModifiedBy: ywyz
@Github: https://github.com/ywyz
@LastEditors: ywyz
@LastEditTime: 2019-07-05 16:05:28
'''
weightInPounds = eval(input("Enter weight in pounds:"))
heightInInches = eval(input("Enter height in inches:"))
weightInKilos = weightInPounds * 0.45359237
heightInMeters = heightInInches * 0.0254
bmi = weightInKilos / heightInMeters**2
print("BMI is ", bmi)
