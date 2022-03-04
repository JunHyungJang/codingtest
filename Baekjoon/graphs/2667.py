n = int(input())

graph = []

for i in range(n):
    k = list(map(int,input()))
    graph.append(k)


def dfs(t):
    global d
    x = t[0]
    y = t[1]
    visited[x][y] = True
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<n and 0<=ny<n :
            # print(nx,ny)
            # print(visited)
            if visited[nx][ny] == False:
                # print(graph)
                if graph[nx][ny] == 1:
                    d+=1
                    dfs([nx,ny])
    return d

answer= 0
result = []
visited = [[False] * n for i in range(n)]
for i in range(n):
    for j in range(n):
        if visited[i][j] == False:
            if graph[i][j] == 1:
                t = [i,j]
                d = 0
                dfs_result = dfs(t)
                answer+=1
                result.append(dfs_result+1)

print(answer)
# print(result)
result.sort()
for i in result:
    print(i)

