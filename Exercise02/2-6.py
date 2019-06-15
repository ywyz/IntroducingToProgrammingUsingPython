#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-06-07 17:03:02
# @Author  : ywyz (admin@ywyz.tech)
# @Version : 1.0.0
# Compute Subtotal
number = eval(input("Enter a number between 0 and 1000: "))
lastNumber = number % 10
middleNumber = number // 10 % 10
firstNumber = number // 100
total = lastNumber + middleNumber + firstNumber
print("The sum of digits is ", total)
