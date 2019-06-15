#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-06-07 18:59:37
# @Author  : ywyz (admin@ywyz.tech)
# @Version : 1.0.0
# Compute years
minuteNumbers = eval(input("Enter the number of minutes: "))
days = minuteNumbers // 60 // 24 % 365
years = minuteNumbers // 60 // 24 // 365
print(minuteNumbers, "minutes is approximately ",
      years, " years and ", days, "days.")
