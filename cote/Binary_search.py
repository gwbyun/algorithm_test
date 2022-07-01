#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 30 20:35:23 2022

@author: gw
"""



def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search(array,target,start,mid-1)
    else:
    #array[mid] < target:
        return binary_search(array,target,mid+1,end)



n,target = list(map(int,input().split()))
array = list(map(int,input().split()))

result = binary_search(array, target, 0 ,n-1)
if result == None:
    print("nothing")
else:
    print(result + 1)