'''
@Date: 2019-11-10 20:18:20
@Author: ywyz
@LastModifiedBy: ywyz
@Github: https://github.com/ywyz
@LastEditors: ywyz
@LastEditTime: 2019-11-10 20:33:06
'''
from conversiontempersion import fahrenheitToCelsiud
from conversiontempersion import celsiusToFahrenheit

print("----------------------------------------------------------------------\
        ----------------------------------")
print("      Celsius       |        Fahrenheit       ||       Fahrenheit      \
           |         Celsius        ")
print(
    "-------------------------------------------------------------------------\
        -------------------------------")
celsius = 40
fahrenheit = 120
for n in range(10):
    print(format(celsius, "11.1f"),
          "        |",
          format(celsiusToFahrenheit(celsius), "13.1f"),
          end=" ")
    print("          ||", end=" ")
    print(format(fahrenheit, "11.1f"),
          "             |",
          format(fahrenheitToCelsiud(fahrenheit), "13.1f"),
          end=" ")
    print("")
    celsius -= 1
    fahrenheit -= 10
