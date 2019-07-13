'''
@Date: 2019-07-04 16:25:52
@Author: ywyz
@LastModifiedBy: ywyz
@Github: https://github.com/ywyz
@LastEditors: ywyz
@LastEditTime: 2019-07-04 17:07:52
'''
speed, acceleration = eval(input("Enter speed and acceleration: "))
mininumRunwayLength = speed**2 / (2 * acceleration)
print("The mininum runway length for this airplane is :", mininumRunwayLength)
