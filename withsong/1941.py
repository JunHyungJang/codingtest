# import sys

# graph = []
# for i in range(5):
#     k = list((input()))
#     graph.append(k)

# visited = [[False]* 5 for i in range(5)]


# cnt = 0
# c_Y = 0
# c_S = 0
# answer = 0
# lst = []
# # print(graph)

# def back(i,j):
#     global cnt
#     global c_S
#     global c_Y
#     global answer
#     global lst

#     dx = [1,-1,0,0]
#     dy = [0,0,1,-1]
#     # print(cnt,c_S)
#     if cnt == 7:
#         if c_S>=4:
#             print(lst)
#             answer+=1
#         return
    

#     for k in range(4):
#         nx = i + dx[k]
#         ny = j + dy[k]

#         if 0<=nx<5 and 0<=ny<5:
#             if not visited[nx][ny]:
#                 if graph[nx][ny] == "Y":
#                     c_Y+=1
#                     cnt+=1
#                     lst.append((nx,ny))
#                     back(nx,ny)
#                     lst.remove((nx,ny))
#                     cnt-=1
#                     c_Y-=1
#                 elif graph[nx][ny] == "S":
#                     c_S+=1
#                     cnt+=1
#                     lst.append((nx,ny))
#                     back(nx,ny)
#                     lst.remove((nx,ny))
#                     c_S-=1
#                     cnt-=1


# for i in range(5):
#     for j in range(5):
#         if graph[i][j] == 'S':
#             c_S+=1
#             cnt+=1
#             back(i,j)
#             c_S-=1
#             cnt-=1
#         elif graph[i][j] == "Y":
#             c_Y+=1
#             cnt+=1
#             back(i,j)
#             c_Y-=1
#             cnt-=1
#         visited[i][j] = True


# print(answer)

graph = []

for i in range(5):
    k = list(input())
    graph.append(k)


answer = 0

gvisited = [[False] * 5 for i in range(5)]

lst = []

def bfs(i,j):
    global answer
    global cnt
    global c_S
    global c_Y
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    if cnt == 7:
        if lst[0] == (1,0):
            print(lst)
            print(c_S)

        if c_S>=4:
            answer+=1
        return
    

    for k in range(4):
        nx = i + dx[k]
        ny = j + dy[k]

        if 0<=nx<5 and 0<=ny<5:
            if not visited[nx][ny] and not gvisited[nx][ny]:
                if graph[nx][ny] == "Y":
                    c_Y+=1
                    cnt+=1
                    visited[nx][ny] = True
                    lst.append((nx,ny))
                    bfs(nx,ny)
                    lst.remove((nx,ny))

                    visited[nx][ny] = False
                    cnt-=1
                    c_Y-=1
                elif graph[nx][ny] == "S":
                    c_S+=1
                    cnt+=1
                    lst.append((nx,ny))
                    visited[nx][ny] = True

                    bfs(nx,ny)
                    visited[nx][ny] = False
                    lst.remove((nx,ny))
                    c_S-=1
                    cnt-=1

    
    

for i in range(5):
    for j in range(5):
        cnt = 0
        c_Y = 0
        c_S = 0

        visited = [[False] * 5 for i in range(5)]
        visited[i][j] = True
        cnt+=1
        lst.append((i,j))
        if graph[i][j] == 'Y':
            c_Y+=1
        elif graph[i][j] == 'S':
            c_S+=1
        bfs(i,j)
        lst.remove((i,j))
        
        gvisited[i][j] = True


print(answer)