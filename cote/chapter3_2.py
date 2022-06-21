#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 21 19:11:17 2022

@author: gw
"""

n, m ,k = list(map(int,input().split()))
data = list(map (int, input().split()))

data.sort()
first = data[n-1]
second = data[n-2]

result = 0

count = int(m/(k+1))*k
count += m % (k+1)

result += (count)* first
result += (int(m/(k+1)))*second

print(result)
