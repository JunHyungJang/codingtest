from collections import deque

def bfs(a,b, chess,c,d,n):
    dx = [-1, -2, -2, -1, 1, 2, 2, 1]
    dy = [2, 1, -1, -2, -2, -1, 1, 2]       

    queue= deque()
    queue.append([a,b])
    chess[a][b] = 1
    while queue:
        x,y = queue.popleft()
        if x == c and y == d:
            return chess[x][y]-1
        for i in range(len(dx)):
            i_x = x+dx[i]
            i_y = y+dy[i]
            
            if 0<=i_x<=n-1 and 0<=i_y<=n-1 and chess[i_x][i_y] == 0:
                queue.append([i_x,i_y])
                
                chess[i_x][i_y] = chess[x][y] + 1
               
        
           

t = int(input())

for i in range(t):
    n = int(input())
    a,b = map(int,input().split())
    c,d = map(int,input().split())

    chess = [[0] * n for i in range(n)]

    print(bfs(a,b,chess,c,d,n))


