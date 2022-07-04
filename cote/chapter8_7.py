#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  4 19:09:00 2022

@author: gw
"""

n = int(input())
d = [0] * 1001

d[1] = 1
d[2]= 3
for i in range(3, n+1):
    d[i] = (d[i-1] +2 * d[i-2]) % 796796
    
    
print(d[n])