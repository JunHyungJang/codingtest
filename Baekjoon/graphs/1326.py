import sys
from collections import deque
def bfs(start):
    flag = 0 
    queue = deque()
    queue.append(start)

    # visited[start] = 1
    while queue:
        t = queue.popleft()
        for i in range(t,N,arr[t]):
            # print(i,visited)
            if visited[i] == -1:
                queue.append(i)
                # print(i,t)
                visited[i]= visited[t]+1
                if i == end:
                    return visited[i]
        for j in range(t,-1,-arr[t]):
            if visited[j] == -1:
                queue.append(j)
                visited[j] = visited[t] + 1
                if j == end:
                    return visited[j]
        
    return -1


N = int(input())

arr = list(map(int,input().split()))

visited = [-1] * N
a,b = map(int,input().split())

start = a-1
end = b -1
visited[start] = 0







print(bfs(start))