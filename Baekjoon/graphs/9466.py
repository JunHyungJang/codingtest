from collections import deque
import sys
sys.setrecursionlimit(10**6)
T = int(input())

def dfs(i):
    global cnt
    cycle.append(i)
    visited[i] = True
    # print(cycle)
    if visited[graph[i]] == True:
        if graph[i] in cycle:
            cnt += len(cycle[cycle.index(graph[i]):])
        return
    else:
        dfs(graph[i])



for i in range(T):
    n = int(input())
    graph = [0]
    cnt = 0
    k = (list(map(int,input().split())))
    for i in k:
        graph.append(i)
    visited =[False] * (n+1)
    # print(graph)
    for i in range(1,n+1):
        if not visited[i]:
            cycle = []
            dfs(i)
    print(n-cnt)

