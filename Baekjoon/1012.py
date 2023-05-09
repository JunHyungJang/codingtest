import sys
from collections import deque


def bfs(arr,root):
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    
    queue = deque()
    queue.append(root)

    x,y = root
    arr[x][y] = 0
    print(x,y)

    while queue:
        x,y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]            

            if nx <0 or ny <0 or nx >= N or ny >= M :
                continue
            if arr[nx][ny] == 1:
                queue.append((nx,ny))
                arr[nx][ny] = 0

    return



t = int(input())
cnt = 0
for i in range(t):
    M,N,k = map(int,input().split())
    arr = [[0 for i in range(M)] for i in range(N)]
    # print(arr)
    for j in range(k):
        m,n = map(int,input().split())
        arr[n][m] = 1

    for x in range(N):
        for y in range(M):
            if arr[x][y] ==1:
                bfs(arr,(x,y))
                cnt+=1
    
    print(cnt)
    cnt = 0
