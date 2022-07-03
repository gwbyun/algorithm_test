#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  3 13:21:28 2022

@author: gw
"""

n, m = map(int,input().split())

array= list(map(int,input().splist()))

start = 0
end = max(array)

result = 0
while(start <= end):
    total = 0
    mid = (start + end) // 2
    for x in array:
        if x > mid:
            total += x - mid
        if total < m :
            end = mid - 1
        else:
            result = mid
            start = mid + 1
    
print(result)
