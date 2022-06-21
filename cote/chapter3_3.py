#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 21 19:27:48 2022

@author: gw
"""

n,m = map(int,input().split())

#array = [[0]*m for _ in  range(n)]
result = 0

for i in range(n):
    data = list(map(int,input().split()))
    minval= min(data)
    result = max(result, minval)
    
print(result)
