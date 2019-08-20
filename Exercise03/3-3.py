'''
@Date: 2019-08-17 19:16:52
@Author: ywyz
@LastModifiedBy: ywyz
@Github: https://github.com/ywyz
@LastEditors: ywyz
@LastEditTime: 2019-08-18 20:24:02
'''
import math

radius = 6371.01
x1, y1 = 35.2270869, -80.8431267  # Charlotte
x2, y2 = 32.0835407, -81.0998342  # Savannah
x3, y3 = 28.5383355, -81.3792365  # Orlando
x4, y4 = 33.7489954, -84.3879824  # Atlanta
y1y2 = y1 - y2

x1x2 = radius * math.acos(
    math.sin(math.radians(x1)) * math.sin(math.sin(math.radians(x2))) +
    math.cos(math.radians(x1)) * math.cos(math.radians(x2)) *
    math.cos(math.radians(y1 - y2)))

x1x4 = radius * math.acos(
    math.sin(math.radians(x1)) * math.sin(math.sin(math.radians(x4))) +
    math.cos(math.radians(x1)) * math.cos(math.radians(x1)) *
    math.cos(math.radians(y1 - y4)))

x2x4 = radius * math.acos(
    math.sin(math.radians(x2)) * math.sin(math.sin(math.radians(x4))) +
    math.cos(math.radians(x2)) * math.cos(math.radians(x4)) *
    math.cos(math.radians(y2 - y4)))

s1 = (x1x2 + x1x4 + x2x4) / 2
area1 = (s1 * (s1 - x1x2) * (s1 - x1x4) * (s1 - x2x4))**0.5

x3x4 = radius * math.acos(
    math.sin(math.radians(x3)) * math.sin(math.sin(math.radians(x4))) +
    math.cos(math.radians(x3)) * math.cos(math.radians(x4)) *
    math.cos(math.radians(y3 - y4)))

x2x3 = radius * math.acos(
    math.sin(math.radians(x2)) * math.sin(math.sin(math.radians(x3))) +
    math.cos(math.radians(x2)) * math.cos(math.radians(x3)) *
    math.cos(math.radians(y2 - y3)))

s2 = (x2x4 + x3x4 + x2x3) / 2
area2 = (s2 * (s2 - x2x4) * (s2 - x3x4) * (s2 - x2x3))**0.5

area = area1 + area2

print("The area between four area is", area, "square kilometers.")
