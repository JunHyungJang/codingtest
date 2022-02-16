import heapq
import sys


def dijkstra(start,end):
    heap = []
    dist[start] = 0
    heapq.heappush(heap,(0,start))

    while heap:
        w, node = heapq.heappop(heap)

        if dist[node] < w:
            # print(heap)
            # print("K", w, dist[node])
            continue
        
        for next_node, next_w in graph[node]:
            distance = w+next_w

            if distance < dist[next_node]:
                dist[next_node] = distance
                heapq.heappush(heap,(distance,next_node))
                print(dist)
        
            # print(dist)



input = sys.stdin.readline
INF = sys.maxsize

n = int(input())
m = int(input())

dist = [INF]*(n+1)
graph = [[] for i in range(n+1)]

for i in range(m):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))

start , end = map(int,input().split())

dijkstra(start,end)

# print(dist)
print(dist[end])
