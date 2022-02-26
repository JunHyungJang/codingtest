import sys
import heapq

INF = sys.maxsize

n,m,x = map(int,input().split())

dpgo = [INF] * (n+1)
dpback = [INF] *(n+1)

graphgo = [[] for i in range(n+1)]
graphback = [[]for i in range(n+1)]


for i in range(m):
    a,b,c = map(int,input().split())
    graphgo[a].append([b,c])
    graphback[b].append([a,c])

dpgo[x] = 0
dpback[x] = 0

def dij(x,dp,graph):
    q = []
    heapq.heappush(q, (dp[x], x))

    while q:
        w, node = heapq.heappop(q)

        if dp[node] < w:
            continue
        else:
            for next_node, dist in graph[node]:
                next_w = w + dist
                if dp[next_node] > next_w:
                    dp[next_node] = next_w
                    heapq.heappush(q,(next_w, next_node))

answer = [0] * (n+1)

dij(x,dpgo,graphgo)
dij(x,dpback,graphback)
for i in range(1,n+1):
    answer[i] +=dpgo[i]
    answer[i] +=dpback[i]

print(max(answer))

# n,m,x = map(int,input().split())

# graph = [[INF] * (n+1) for i in range(n+1)]
# # dpgo = [INF] * (n+1)
# # dpgo[x] = 0

# # dpback = [INF] * (n+1)



# for i in range(m):
#     a,b,c = map(int,input().split())
#     graph[a][b]= c


# for k in range(1,n+1):
#     for i in range(1,n+1):
#         for j in range(1,n+1):
#             graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

# dp = [ 0 for i in range(n+1)]

# for i in range(1,n+1):
#     dp[i] = graph[i][x] + graph[x][i]

# # print(dp)
# print(max(dp))

