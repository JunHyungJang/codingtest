import sys
from collections import deque
sys.setrecursionlimit(10**6)

input = sys.stdin.readline
N,M = map(int,input().split())

graph = [[]for i in range(N+1)]


for i in range(M):
    a,b = map(int,input().split())
    # graph[a].append(b)
    graph[b].append(a)

# print(graph)

def dfs(v,cnt):
    visited[v] = True
    for i in graph[v]:
        # print(cnt)
        if not visited[i]:
            # print(i)
            # visited[i] = True
            dfs(i,cnt+1)
    
    return cnt

answer = []
for i in range(1,N+1):
    visited = [False] * (N+1)
    # answer.append(dfs(i,0))
    print(dfs(i,0))
   

for i in range(N):
    if answer[i] == max(answer):
        print(i+1, end = " ")
    