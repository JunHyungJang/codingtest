import sys
import heapq
from collections import deque

# def dijkstra():
#     heap = []
#     heapq.heappush(heap, (0,1))


#     while heap:
#         w, node = heapq.heappop(heap)

#         for next_node, next_weight in graph[node]:
#             distance = w+next_weight

#             if dist[next_node] > distance:
#                 dist[next_node] = distance
#                 heapq.heappush(heap,(distance,next_node))

def finding(w,k):


def track(k):
    for i in incom:
        if i[0] == 1:
            answer[k].append(i[1])
        else:
            finding(i[1],k)

    



input = sys.stdin.readline
INF = sys.maxsize

n,m,k = map(int,input().split())

graph = [[]for i in range(n+1)]

dist = [INF for i in range(n+1)]
dist[1] = 0
# klist = [[]for i in range(n+1)]

incom_dict = {}
answer = [[]for i in range(n+1)]
incom = [[]for i in range(n+1)]
for i in range(m):
    a,b,c = map(int,input().split())
    graph[a].append([b,c])
    incom[b].append([a,c])
    # incom_dict[b] = [a,c]
print(incom)
# dijkstra()
print(graph)
print(dist)