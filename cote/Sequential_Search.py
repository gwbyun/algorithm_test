#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 30 19:47:54 2022

@author: gw
"""


'''
array = [0]*n

for i in range(n):
    array[i] = int(input())
    
print(array)
'''
input_data = input().split()
print(type(input_data))
n= int(input_data[0])
target = input_data[1]

#array = [0]*n
array = input().split()


def sequential_search(n, target, array):
    for i in range(n):
        if array[i] == target:
            return i+1

print(sequential_search(n, target, array),array)