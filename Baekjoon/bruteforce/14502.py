from collections import deque
from itertools import combinations
import sys

import copy

input = sys.stdin.readline
INF = sys.maxsize


n, m = map(int,input().split())

mapp = []
virus_list = []
empty_list = []

for i in range(n):
    k = list(map(int,input().split()))
    mapp.append(k)
    for j in range(len(k)):
        if k[j] == 2:
            virus_list.append([i,j])
        if k[j] == 0:
            empty_list.append([i,j])

wall_list = list(combinations(empty_list,3))
# print(mapp)
original_map = copy.deepcopy(mapp)
# print(original_map)


def bfs():
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    while q:
        x,y = q.pop()
        for i in range(len(dx)):
            new_x = x + dx[i]
            new_y = y + dy[i]
            if 0<= new_x <n and 0<=new_y<m and mapp[new_x][new_y] == 0:
                mapp[new_x][new_y] = 2
                q.append([new_x,new_y])
                

result = 0

check = 0
# print(wall_list)

for wall in wall_list:
    # print(virus)
    # print(mapp)

    #making mapp
    mapp = [[0]*m for i in range(n)]
    for c in range(n):
        for v in range(m):
            mapp[c][v] = original_map[c][v]
    
    answer = 0
    for i in wall:
        mapp[i[0]][i[1]] =1
    # print(mapp)
    # virus bfs
    
    for z in virus_list:
        q = deque()
        q.append(z)
        bfs()
    
    # checking area 
    for k in range(n):
        for t in range((m)):
            if mapp[k][t] == 0:
                answer+= 1
    # print(mapp)
    
    result = max(result, answer)
    # print(result)


# print(mapp)
# print(original_map)
# print(ori_map)
print(result)
