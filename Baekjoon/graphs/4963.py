import sys
from collections import deque


def bfs(t):
    global w
    global h
    global visited
    
    dx = [1,-1,0,0,1,1,-1,-1]
    dy = [0,0,1,-1,1,-1,1,-1]
    q = deque()
    q.append(t)
    visited[t[0]][t[1]] = True


    while q:
        x, y = q.popleft()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<h and 0<=ny< w:
                # print(nx,ny)
                if visited[nx][ny] == False and graph[nx][ny] == 1:
                    visited[nx][ny] = True
                    q.append([nx,ny])



while 1:
    answer = 0
    w,h = map(int,input().split())

    if w == 0 and h == 0:
        break
    graph = []

    for i in range(h):
        k = list(map(int,input().split()))
        graph.append(k)
    
    visited = [[False] * w for i in range(h)]
    # print(visited)
    for x in range(h):
        for y in range(w):
            if visited[x][y] == False:
                if graph[x][y] == 1:
                    answer+=1
                    bfs([x,y])
    
    print(answer)


