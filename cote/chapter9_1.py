#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  5 21:27:43 2022

@author: gw
"""

import sys
#input = sys.stdin.readline
INF = int(1e9)

n,m = map(int,input().split())

#get start node number
start = int(input())
#node information
graph = [[]for i in range(n+1)]
#print(graph)

visited = [False] * (n+1)
distance = [INF] * (n+1)

for _ in range (m):
    a,b,c = map(int, input().split())
    # a to b distance c
    graph[a].append((b,c))

#print(graph)

def get_smallest_node():
    min_value = INF
    index = 0
    #just initialize
    
    for i in range(1,n+1):
        if (distance[i] < min_value) and not (visited[i]):
            min_value = distance[i]
            index = 1
        return index
    
def dijkstra(start):
    distance[start] = 0
    visited[start] = True
    for j in graph[start]:
        print(graph[start])
        distance[j[0]]=j[1]
        print(j[0])
        print(distance[j[0]])
        print(distance)
    for i in range(n-1):
        now = get_smallest_node()
        visited[now] = True
        
        for j in graph[now]:
            cost = distance[now] + j[i]
            if cost < distance[j[0]]:
                distance[j[0]] = cost

dijkstra(start)

for i in range(1, n+1):
    
    if distance[i] == INF:
        pass
        #print('infinity')
    #else:
