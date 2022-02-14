import sys
input = sys.stdin.readline

sys.setrecursionlimit(1000000)

def dfs(graph,w,n,m):
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]

    graph[w[0]][w[1]] = -1
    for i in range(4):
        x = w[0]+dx[i]
        y = w[1]+dy[i]
        if 0<=x<n and 0<=y<m :
            if graph[x][y] == 0:
                global square
                square+=1
                # print(square)

                dfs(graph,[x,y],n,m)

    


n,m,k = map(int,input().split())

graph = [[0] * m for i in range(n)]

location  = []
for i in range(k):
    r = list(map(int,input().split()))
    location.append(r)

for j in range(k):
    t = location[j]
    x1,y1,x2,y2 = t[0], t[1], t[2], t[3]
    # print(x1,y1,x2,y2)
    s_x = min(x1,x2)
    s_y = min(y1,y2)

    x_i = abs(x1-x2)
    y_i = abs(y1-y2)

    # print(x1,y1)
    for i in range(x_i):
        for k in range(y_i):
            graph[y1+k][x1+i] = 1
    
count = 0
result = []
# print(graph)
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            square= 1
            dfs(graph,[i,j],n,m)
            # print(square)
            # print(graph)
            # result.append(t)
            result.append(square)
            count+=1
result.sort()
print(count)
for i in result:
    print(i, end = " ")
# print(graph)