#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 21 15:52:23 2022

@author: gw
"""

money = int(input())

result = 0

cent = [500, 100, 50, 10]

for i in cent:
    result += money // i
    money = money % i

print(result)

