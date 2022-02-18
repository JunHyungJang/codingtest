from collections import deque
import sys
input = sys.stdin.readline

n, m =map(int,input().split())

picture = []

for i in range(n):
    k = list(map(int,input().split()))
    picture.append(k)

visited = [[False]*m for i in range(n)]

def bfs(start):
    result = 1
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    q= deque()
    q.append(start)
    visited[start[0]][start[1]] =True
    while q:
        x,y = q.popleft()
        for i in range(len(dx)):
            new_x = x+dx[i]
            new_y = y+dy[i]
            if 0<=new_x<n and 0<=new_y<m and visited[new_x][new_y] == False:
                if picture[new_x][new_y] == 1:
                    visited[new_x][new_y] = True
                    q.append((new_x,new_y))
                    result+=1
    
    return result

final = []
for i in range(n):
    for j in range(m):
        if visited[i][j] == False and picture[i][j] == 1:
            answer = bfs((i,j))
            final.append(answer)

if len(final) == 0:
    print(0)
    print(0)
else:
    print(len(final))
    print(max(final))

# print(final)
