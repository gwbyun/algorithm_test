#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  1 20:22:44 2022

@author: gw
"""

#Memoization

d = [0] * 100

#Fibonacci Function top_down dinamic programing
def fibo(x):
    if x ==1 or x==2:
        return 1
    
    if d[x] != 0:
        return d[x]
    
    d[x] = fibo(x-1) + fibo(x-2)
    return d[x]

print(fibo(99))
print(d)