import sys
from collections import deque

n = int(input())

k = int(input())

arr = [[] for i in range(n+1)]

for i in range(k):
    a,b = map(int,input().split())
    arr[a].append(b)
    arr[b].append(a)

answer = 0

visited = [False] * (n+1)


def bfs(arr):
    cnt = 0

    start = 1
    queue = deque()
    queue.append(start)

    while queue:
        k = queue.popleft()
        visited[start] = True
        # print(arr)
        # print(arr[k])
        for i in range(len(arr[k])):
            if visited[arr[k][i]] == False:
                visited[arr[k][i]] = True
                queue.append(arr[k][i])
                cnt +=1
    print(cnt)
    
    return

bfs(arr)


