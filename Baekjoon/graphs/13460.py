from collections import deque

n,m = map(int,input().split())

# print(a,b)
graph = []
for i in range(n):
    k = list(input())
    for j in range(m):
        if k[j] == 'R':
            r = [i,j]
        if k[j] == 'B':
            b = [i,j]
    graph.append(k)

# print(r,b,graph)
# print(a,b)
visited = [[[[False] * m for i in range(n)] for i in range(m)] for i in range(n)]

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def move(rx,ry,dx,dy):
    c = 0
    while graph[rx+dx][ry+dy] != '#' and graph[rx][ry] != 'O':
        rx += dx
        ry += dy
        c +=1
    return rx,ry,c
def bfs():
    q = deque()
    q.append((r[0],r[1],b[0],b[1],1))
    visited[r[0]][r[1]][b[0]][b[1]] = True
    while q:
        rx,ry,bx,by,cnt = q.popleft()
        if cnt > 10:
            break
        for i in range(4):
            nrx,nry,rd = move(rx,ry,dx[i],dy[i])
            nbx,nby,bd = move(bx,by,dx[i],dy[i])
            if graph[nbx][nby] != "O":
                if graph[nrx][nry] == "O":
                    print(cnt)
                    return
                if nbx == nrx and nby == nry :
                    if rd > bd :
                        nrx -=dx[i]
                        nry -=dy[i]
                    else:
                        nbx -=dx[i]
                        nby -=dy[i]
                if visited[nrx][nry][nbx][nby] == False:
                    visited[nrx][nry][nbx][nby] == True
                    q.append((nrx,nry,nbx,nby,cnt+1))
    print(-1)

bfs()