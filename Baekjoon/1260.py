import sys
from collections import deque



def dfs(V,result):
    visited[V] = True
    result.append(V)
    for i in arr[V]:
        if not visited[i]:
            dfs(i,result)
    
    return result 

def dfs2(V,result):
    need_visited = deque()
    need_visited.append(V)
    while need_visited:
        node = need_visited.popleft()
        if not visited[node]:
            print(node)
            visited[node] = True
            result.append(node)
            need_visited.append(node)
    return result

def bfs(V):
    queue = deque()
    queue.append(V)
    visited[V] = True
    while queue:
        k = queue.popleft()
        result.append(k)
        # print(result)
        for i in arr[k]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
    
    return result


N,M,V = map(int,input().split())

visited = [False] * (N+1)

arr = [[] for i in range(N+1)]


result = []
for i in range(M):
    a,b = map(int,input().split())
    arr[a].append(b)
    arr[b].append(a)

for k in arr:
    k.sort()

result = []
print(dfs2(V,result))
result = []
visited = [False] * (N+1)

print(bfs(V))
# print(dfs(V,result))

    
        