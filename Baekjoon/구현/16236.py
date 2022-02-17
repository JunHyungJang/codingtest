# import sys
# import copy
# from collections import deque

# input = sys.stdin.readline



# n = int(input())

# graph = []


# for i in range(n):
#     v = list(map(int,input().split()))
#     graph.append(v)
#     if 9 in v:
#         start = [i,v.index(9)]

# graph[start[0]][start[1]] = 0 

# size =2
# def bfs(graph,start):
#     global size
#     print(start) 

#     distance = [[0]*n for i in range(n)]
#     visited = [[False]*n for i in range(n)]
    
#     dx = [-1,0,1,0]
#     dy = [0,-1,0,1]

#     q = deque()
#     q.append(start)
#     visited[start[0]][start[1]] = True
#     # print(visited)

#     while q:
#         x,y = q.popleft()
#         for i in range(len(dx)):
#             new_x = x + dx[i]
#             new_y = y + dy[i]
#             if 0<=new_x<n and 0<=new_y<n :
#                 if not visited[new_x][new_y]:
#                     if graph[new_x][new_y] > size:
#                         pass
#                     if graph[new_x][new_y] == 0 or graph[new_x][new_y] == size:
#                         distance[new_x][new_y] = distance[x][y] + 1
#                         visited[new_x][new_y] = True
#                         # print(visited)
#                         # print(distance)
#                         q.append([new_x,new_y])
#                         # print(q)
#                         # print(new_x, new_y, "move")
#                     if 0< graph[new_x][new_y] < size:
#                         # size+=1
#                         dist = distance[x][y] +1
#                         # print(dist, "dist")
#                         # print(new_x,new_y, "answer")
#                         # graph[new_x][new_y] = 0
#                         # print(distance)
#                         return dist, new_x, new_y
#                     # print(q)
#                 # print(distance,x,y)
#     return -1, -1, -1



# def multi_bfs(graph,k):
#     global size
#     result = 0
#     eat = 0
#     while True:
#         dist, new_x, new_y = bfs(graph,k)
#         # print(new_x,new_y,dist)
#         if dist == -1:
#             break
#         else:
#             eat+=1
#             if eat == size:
#                 size+=1
#                 eat =0
#             result+= dist
#             k = [new_x, new_y]
#             graph[new_x][new_y] = 0
            

#     return result

# print(multi_bfs(graph,start))

import sys,collections
shark_x, shark_y = 0,0
shark_size = 2
eat_cnt = 0
fish_cnt = 0
fish_pos = []
time = 0
dx = (0,0,1,-1)
dy = (1,-1,0,0)
n = int(sys.stdin.readline())
board = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
for i in range(n):
    for j in range(n):
        if 0 < board[i][j] <=6:
            fish_cnt +=1
            fish_pos.append((i,j))
        elif board[i][j] == 9:
            shark_x, shark_y = i,j
board[shark_x][shark_y]=0

def bfs(shark_x,shark_y):
    q = collections.deque([(shark_x,shark_y,0)])
    dist_list = []
    visited = [[False]*n for _ in range(n)]
    visited[shark_x][shark_y] = True
    min_dist = int(1e9)
    while q:
        x,y,dist = q.popleft()
        for i in range(4):
            xx = dx[i]+x
            yy = dy[i]+y
            if 0<=xx<n and 0<=yy<n and not visited[xx][yy]:
                if board[xx][yy] <= shark_size:
                    visited[xx][yy] = True
                    if 0<board[xx][yy]<shark_size:
                        min_dist = dist
                        dist_list.append((dist+1,xx,yy))
                    if dist+1 <= min_dist:
                        q.append((xx,yy,dist+1))
    if dist_list:
        dist_list.sort()
        return dist_list[0]
    else:
        return False

while fish_cnt :
    result = bfs(shark_x,shark_y)
    if not result:
        break
    shark_x,shark_y = result[1],result[2]
    time +=result[0]
    eat_cnt+=1
    fish_cnt-=1
    if shark_size == eat_cnt:
        shark_size +=1
        eat_cnt =0
    board[shark_x][shark_y] = 0

print(time)