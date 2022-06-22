#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 18:19:05 2022

@author: gw
"""

import time

start_time = time.time()

n, k = map(int, input().split())

count = 0

while True:
    if n%k == 0 :
        n = n//k
        count = count +1
    else:
        n = n-1
        if n==0:
            break
        count =count +1
print(count)

'''
while n >= k :
    while n % k !=0:
        n -=1
        count +=1
    
    n//=k
    count +=1
    
while n>1:
    n-=1
    count+=1

print(count)
'''
end_time=time.time()
print("time :", end_time - start_time)
     