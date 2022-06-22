#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 20:17:18 2022

@author: gw
"""
import time

n = int(input())
move =list(map(ord, input().split()))
start= time.time()
#print(type(move))
#array = [[0]*n for _ in  range(n)]
position_x = 1
position_y = 1

for i in  move:
    #print(i)
    if i == ord('R'):
        if position_x <= n:
            position_x =position_x  + 1
            #print(position_y,position_x)
    elif i == ord('L'):
        if position_x > 1:
            position_x = position_x - 1 
            #print(position_y,position_x)
    elif i ==ord('U'):
        if position_y >1 :
            position_y = position_y - 1      
            #print(position_y,position_x)   
    elif i == ord('D'):
        if position_y <= n:
            position_y = position_y + 1        
            #print(position_y,position_x)
print(position_y,position_x)
end= time.time()
print(end-start)