#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul  2 18:25:56 2022

@author: gw
"""

n = int(input())
array=[]
for i in range(n):
    array.append(int(input()))
print(array)

array = sorted(array,reverse=True)

print(array)