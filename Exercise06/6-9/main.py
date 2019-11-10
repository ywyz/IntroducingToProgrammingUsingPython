'''
@Date: 2019-11-10 20:46:25
@Author: ywyz
@LastModifiedBy: ywyz
@Github: https://github.com/ywyz
@LastEditors: ywyz
@LastEditTime: 2019-11-10 20:53:14
'''
from conversionlength import footToMeter
from conversionlength import meterToFoot

print("---------------------------------------------------------------------- \
----------------------------------")
print("         Feet        |           Meters       ||          Meters      \
   |           Feet        ")
print(
    "-------------------------------------------------------------------------\
-------------------------------")
feet = 1.0
meters = 20.0
for n in range(10):
    print(format(feet, "11.1f"),
          "         |",
          format(footToMeter(feet), "15.3f"),
          end=" ")
    print("       ||", end=" ")
    print(format(meters, "11.1f"),
          "            |",
          format(meterToFoot(meters), "15.3f"),
          end=" ")
    print("")
    feet += 1
    meters += 5
