#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 24 16:19:23 2022

@author: gw
"""

n =input()
n=int(n)
count = 0
time= [0,0,0]
for i in range(n+1):
    time[0]=i
    for j in range(60):
        time[1]=j
        for k in range(60):
            time[2]=k
            #print(time)
            print(''.join(a for a in list(map(str,time))))
            b=''.join(a for a in list(map(str,time)))
            c=str(b)
            if '3' in c:
                count += 1
                
print(count)