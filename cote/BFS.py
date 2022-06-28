#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 28 19:33:07 2022

@author: gw
"""

from collections import deque

graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
    ]

visited = [False] * 9

#Define BFS method
def BFS(graph, start, visited):
    queue = deque([start])

    visited[start] = True
    
    while queue:
        v=queue.popleft()
        #print(v, end=' ')
        
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                print(queue)
                
BFS(graph, 1, visited)