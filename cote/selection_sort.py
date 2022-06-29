#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 28 21:55:17 2022

@author: gw
"""

#selection sort
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
    min_index = i
    for j in range (i+1,len(array)):
        if array[min_index]>array[j]:
            print(min_index)
            min_index = j
            print(min_index, i, j)
    array[i], array[min_index] = array[min_index],array[i]
    
print(array)