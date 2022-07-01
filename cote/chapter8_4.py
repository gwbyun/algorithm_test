#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  1 20:35:56 2022

@author: gw
"""

#Memoization
d = [0]*100

d[1]=1
d[2]=1
n=99

for i in range(3,n+1):
    d[i]= d[i-1] + d[i-2]
    
print(d[n])