import heapq
import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline
V,E = map(int,input().split())

K = int(input())

graph = {}

for i in range(E):
    a,b,c = map(int,input().split())
    if a in graph:
        graph[a].append([b,c])
    else:
        graph[a] = [[b,c]]

dist = [float('inf') for i in range(V+1)]
dist[k] = 0


def finding():
    heap = []
    heapq.heappush(heap,[0,s])
    
    while heap:
        w,node = heapq.heappop(heap)

        # if dist[]
        for next_node, i in graph[node]:
            next_w = w + i
            if dist[next_node] > next_w:
                dist[next_node] = next_w
                heapq.heappush(heap,(next_w,next_node))

