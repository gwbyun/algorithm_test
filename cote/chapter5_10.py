#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  1 21:21:43 2022

@author: gw
"""

n, m = list(map(int,input().split()))

graph = []
for i in range(n):
    graph.append(list(map(int,input())))
    
def dfs(x,y):
    if x<= -1 or x>=n or y<=-1 or y>=m:
        return False
    
    if graph[x][y] == 0:
        graph[x][y] = 1
        
        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)
        return True
    return False

result = 0
for i in range(n):
    for j in range(m):
        
        if dfs(i,j) == True:
            result += 1
print(result)