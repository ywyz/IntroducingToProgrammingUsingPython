#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-06-07 15:10:22
# @Author  : ywyz (admin@ywyz.tech)
# @Version : 1.0.0
# Compute gratuity
subtotal, gratuityRate = eval(input("Enter the subtotal and a gratuity rate:"))
gratuity = subtotal * gratuityRate * 0.01
total = subtotal + gratuity
print("The gratuity is", gratuity, "and the total is ", total)
