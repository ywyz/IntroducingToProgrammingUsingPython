#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-06-07 19:01:54
# @Author  : ywyz (admin@ywyz.tech)
# @Version : 1.0.0
# Compute energy
amountWater = eval(input("Enter the amount of water in kilograms: "))
intialTemperature = eval(input("Enter the intial temperature: "))
finalTemperature = eval(input("Enter the final temperature:"))
needEnergy = amountWater * (finalTemperature - intialTemperature) * 4184
print("The energy needed is", needEnergy)