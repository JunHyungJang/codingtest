from collections import deque
import heapq
import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)
INF = sys.maxsize


def dijkstra(s):
    heap = []
    heapq.heappush(heap,(0,s))

    while heap:
        w, node = heapq.heappop(heap)

        if dp[node] < w:
            continue
        
        for next_node,i in graph[node]:
            # print(graph[node])
            next_w = w+i
            # print(next_w, next_node)
            if next_w < dp[next_node]:
                dp[next_node] = next_w
                heapq.heappush(heap,(next_w,next_node))
    
            


v,e = map(int,input().split())

s = int(input())


graph = [[]for i in range(v+1)]
for i in range(e):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))

dp = [INF] * (v+1)
dp[s] = 0

dijkstra(s)

for i in range(1,v+1):
    if dp[i] == INF:
        print("INF")
    else:
        print(dp[i])

