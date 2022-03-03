from collections import deque

def bfs(n,start,blind):
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    
    q = deque()
    q.append(start)
    visited[start[0]][start[1]] = True

    while q:
        # print(q)
        x,y = q.popleft()
        color = graph[x][y]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<n and 0<=ny<n and not visited[nx][ny]:
                if blind == 0:
                    
                    if graph[nx][ny] == color:
                        visited[nx][ny] = True
                        q.append((nx,ny))
                
                elif blind == 1:
                    
                    if color == "R" or color == "G":
                        if graph[nx][ny] == "R" or graph[nx][ny] == "G":
                            visited[nx][ny] = True
                            q.append((nx,ny))
                        
                    elif color == "B":
                        if graph[nx][ny] == "B":
                            visited[nx][ny] = True
                            q.append((nx,ny))

n = int(input())

graph = []
for i in range(n):
    k = list(input())
    graph.append(k)


visited = [ [False] *n for i in range(n)]
answer1=0
for i in range(n):
    for j in range(n):
        if visited[i][j] == False:
            bfs(n,(i,j),0)
            answer1+=1
print(answer1)


visited = [ [False] *n for i in range(n)]
answer2 = 0
for i in range(n):
    for j in range(n):
        if visited[i][j] == False:
            bfs(n,(i,j),1)
            answer2+=1

print(answer2)


            
            
    