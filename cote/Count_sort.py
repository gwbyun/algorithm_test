#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 29 15:10:35 2022

@author: gw
"""

array = [7,5,9,0,3,1,6,2,9,1,4,8,0,5,2]

count = [0] * (max(array) + 1)

for i in range(len(array)):
    count[array[i]] += 1
print(count)
for i in range(len(count)):
    #print(count[i])
    for j in range(count[i]):
        #print(j)
        print(i, end=' ')
    