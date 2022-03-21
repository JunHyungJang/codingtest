import sys
from itertools import combinations
import copy




graph = []

for i in range(4):
    k = []
    t = list(map(int,input().split()))
    for j in range(6):
        r = t[3*j:3*j+3]
        print(r)
        k.append(r)
    graph.append(k)

poss = list(combinations([0,1,2,3,4,5],2))
print(poss)


def back(arr,idx):
    global answer
    if idx == 15:
        answer = 1
        for k in arr:
            if k.count(0)!=3:
                answer = 0
                break
        return
    
    x,y = poss[idx]
    for a,b in ((0,2), (1,1), (2,0)):
        if arr[x][a] >0 and arr[y][b] > 0:
            arr[x][a]-=1
            arr[y][b]-=1
            back(arr,idx+1)
            arr[x][a]+=1
            arr[y][b]+=1

print(answer1)
for i in range(4):
    k = graph[i]
    if k in tarr:
        print(1)
    else:
        print(0)