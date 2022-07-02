#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul  2 18:55:47 2022

@author: gw
"""

n, k = list(map(int,input().split()))
a = list(map(int,input().split()))
b = list(map(int,input().split()))

a.sort()
b.sort(reverse = True)

for i in range(k):
    if a[i] < b[i]:
        a[i],b[i]= b[i],a[i]
    else:
        break
    
print(sum(a))