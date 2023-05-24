from collections import deque

N,M = map(int,input().split())

graph = []

for i in range(N):
    k = list(input())
    for j in range(M):
        if k[j] == 'B':
            b = [i,j]
        if k[j] == 'R':
            r = [i,j]
    graph.append(k)


visited = [[[[False]*M for i in range(N)] for i in range(M) ] for i in range(N)]

def move(x,y,dx,dy):
    c = 0

    while graph[x+dx][y+dy] != '#' and graph[x][y] != 'O':
        x +=dx
        y +=dy
        c+=1
    return x,y,c 


def bfs():
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    q = deque()
    q.append((r[0],r[1],b[0],b[1],1))
    visited[r[0]][r[1]][b[0]][b[1]] = True

    while q:
        rx,ry,bx,by,cnt = q.popleft()
        if cnt > 10 :
            break
    
        for i in range(4):
            nrx,nry,rc = move(rx,ry,dx[i],dy[i])
            nbx,nby,bc = move(bx,by,dx[i],dy[i])
            if graph[nbx][nby] != 'O':
                if graph[nrx][nry] == 'O':
                    print(1)
                    return 
                if nrx == nbx and nry == nby :
                    if rc > bc :
                        nrx -=dx[i]
                        nry -=dy[i]
                    else:
                        nbx -=dx[i]
                        nby -=dy[i]
                if visited[nrx][nry][nbx][nby] == False:
                    visited[nrx][nry][nbx][nby] = True
                    q.append((nrx,nry,nbx,nby,cnt+1))
        
    print(0)
    return 

bfs()

        
