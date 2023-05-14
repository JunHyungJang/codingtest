import sys
sys.setrecursionlimit(100000)

N,M = map(int,input().split())

graph = []
for i in range(N):
    graph.append(list(input()))

dp = [[0]*M for i in range(N)]
# print(graph)

maxdist = -1
visited = [[False]*M for i in range(N)]

def dfs(x,y,dist):
    global maxdist
    maxdist = max(maxdist, dist)
    move = int(graph[x][y])
    change = [[x-move,y], [x+move,y], [x,y-move], [x,y+move]]
    for k in change:
        nx ,ny = k
        if 0<=nx<N and 0<=ny<M and graph[nx][ny] != 'H':
            if visited[nx][ny] == False:
                if dist + 1 > dp[nx][ny]:
                    dp[nx][ny] = dist+1
                    visited[nx][ny] = True
                    dfs(nx,ny,dist+1)
                    visited[nx][ny] = False
            else:
                print(-1)
                exit()

dfs(0,0,1)
print(maxdist)