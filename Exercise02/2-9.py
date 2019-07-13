'''
@Date: 2019-07-04 16:17:36
@Author: ywyz
@LastModifiedBy: ywyz
@Github: https://github.com/ywyz
@LastEditors: ywyz
@LastEditTime: 2019-07-04 16:24:55
'''
temperatureInFahrenheit = eval(
    input("Enter the temperature in Fahrenheit between -58 and 41:"))
windSpeed = eval(input("Enter the wind speed in miles per hour:"))
feelTemperature = 35.74 + 0.6215 * temperatureInFahrenheit - 35.75 * \
    windSpeed**0.16 + 0.4275 * temperatureInFahrenheit * windSpeed**0.16
print("The wind chill index is ", feelTemperature)
