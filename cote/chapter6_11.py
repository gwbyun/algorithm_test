#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul  2 18:37:40 2022

@author: gw
"""

n = int(input())

array = []
for i in range(n):
    input_data = input().split()
    array.append((input_data[0], int(input_data[1])))
    
array = sorted(array, key = lambda student: student[1])

for student in array:
    print(student[0], end = ' ')