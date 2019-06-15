#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-06-07 13:55:55
# @Author  : ywyz (admin@ywyz.tech)
# @Version : 1.0.1
# Compute Volume of cylinder
radiusOfCylinder, lengthOfCylinder = eval(
    input("Enter the radius and length of a cylinder: "))
PI = 3.1415
area = radiusOfCylinder * radiusOfCylinder * PI
volume = area * lengthOfCylinder
print("The area is ", area)
print("The volume is", volume)
