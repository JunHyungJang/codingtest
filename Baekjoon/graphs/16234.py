from collections import deque
import math

N,L,R = map(int,input().split())

graph = []
for i in range(N):
    k = list(map(int,input().split()))
    graph.append(k)
# print(graph)


dx = [1,-1,0,0]
dy = [0,0,1,-1]
def bfs(i,j):
    lst = []
    q = deque()
    q.append((i,j))
    visited[i][j] = True
    lst.append([i,j])
    total = graph[i][j]
    cnt = 1
    while q:
        x,y= q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx < N and 0<=ny<N :
                if visited[nx][ny] == False:
                    if L <= abs(graph[nx][ny] - graph[x][y]) <= R:
                        visited[nx][ny] = True
                        lst.append([nx,ny])
                        q.append((nx,ny))
                        total+=graph[nx][ny]
                        cnt +=1
    
    if len(lst) >1 :
        # print(lst)
        answer = math.floor(total / cnt)
        for k in lst:
            a,b = k
            graph[a][b] = answer
        # print(graph)
        return 1
    # print(graph)
    return 0

result = 0
go = True
while go:
    visited = [[False]*N for i in range(N)]
    go = False 
    for i in range(N):
        for j in range(N):
            if visited[i][j] == False:
                k = bfs(i,j)
                if k:
                    go = True
    if go :
        result+=1
    


print(result)
        