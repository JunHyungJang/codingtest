from re import T
import sys


import sys
import heapq

def dijkstra(start,end):
    heap = []
    heapq.heappush(heap,(0,start))

    while heap:
        w, node = heapq.heappop(heap)

        if dist[node] < w:
            # print(heap)
            # print("K", w, dist[node])
            continue

        for next_node, next_weight in graph[node]:
            distance = next_weight + w

            if distance < dist[next_node]:
                # print(node, next_node)
                # print(trace)
                dist[next_node] = distance
                trace[next_node] = node
                
                


                heapq.heappush(heap,(distance,next_node))

def path(end,start):
    if start in answer:
        return
    else:
        answer.append(trace[end])
        # print(answer)
        path(trace[end], start)




input = sys.stdin.readline

INF = sys.maxsize

n = int(input())
m = int(input())

graph = [[] for i in range(n+1)]
dist = [INF for i in range(n+1)]

for i in range(m):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))

start, end = map(int,input().split())
dist[start] = 0


trace = [[None] for i in range(n+1)]
dijkstra(start,end)
# print(trace)
answer = []
answer.append(end)

path(end,start)

print(dist[end])
print(len(answer))

for i in range(len(answer)):
    print(answer[len(answer)-i-1] , end = " ")



