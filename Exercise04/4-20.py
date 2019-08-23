'''
@Date: 2019-08-23 19:32:32
@Author: ywyz
@LastModifiedBy: ywyz
@Github: https://github.com/ywyz
@LastEditors: ywyz
@LastEditTime: 2019-08-23 19:33:26
'''
import sys

temperatureInFahrenheit = eval(
    input("Enter the temperature in Fahrenheit between -58 and 41:"))
windSpeed = eval(input("Enter the wind speed in miles per hour:"))
if (temperatureInFahrenheit < -58
        or temperatureInFahrenheit > 41) or (windSpeed < 2):
    print("The temperature in Fahrenheit or the wind speed is invalid. ")
    sys.exit()
feelTemperature = 35.74 + 0.6215 * temperatureInFahrenheit - 35.75 * \
    windSpeed**0.16 + 0.4275 * temperatureInFahrenheit * windSpeed**0.16
print("The wind chill index is ", feelTemperature)
