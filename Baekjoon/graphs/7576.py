import sys
from collections import deque
input = sys.stdin.readline


n,m = map(int,input().split())

farm = []
good = []
wall = []

answer = 0

visited = [[False]*n for i in range(m)]



for i in range(m):
    k = list(map(int,input().split()))
    for j in range(n):
        if k[j] == 1:
            good.append((i,j))
            visited[i][j] = True
        if k[j] == -1:
            wall.append((i,j))
    farm.append(k)

# print(len(good))
check = len(good)

dx = [1,-1,0,0]
dy = [0,0,1,-1]
    


def bfs():
    global check
    global answer
    
    q = deque(good)

    while q:
        if check ==0:
            check = len(q)
            answer+=1
        
        x,y = q.popleft()
        check-=1
        # print(check)
        
        
        for i in range(4):
            new_x = x + dx[i]
            new_y = y + dy[i]

            if 0<=new_x<m and 0<=new_y<n:
                if visited[new_x][new_y] == False and farm[new_x][new_y] == 0:
                    visited[new_x][new_y] = True
                    q.append((new_x,new_y))


# print(wall)
bfs()
# print(visited)
def finding():
    for i in range(m):
        for j in range(n):
            if visited[i][j] == False:
                if (i,j) in wall:
                    pass
                else:
                    # print(j,m)
                    print(-1)
                    return
    print(answer)
finding()
# print(visited)
# print(answer)