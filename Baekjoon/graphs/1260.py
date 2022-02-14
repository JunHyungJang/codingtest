from collections import deque
# graph = {}




def dfs(graph, w,visited,result):
    visited[w] = True
    result.append(w)
    for i in graph[w]:
        if not visited[i]:
            dfs(graph,i,visited,result)
    
    return result

def bfs(graph,w,visited,result):
    queue = deque([w])
    visited[w] = True
    while queue:
       
        node = queue.popleft()
        result.append(node)
        for i in graph[node]:
           
            if not visited[i]:
                queue.append(i)
                visited[i] = True
              
    return result

v, e, s = map(int, input().split())
    

graph = [[]for i in range(v+1)]
for i in range(e):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
    graph[a].sort()
    graph[b].sort()

visited = [False] * (v+1)

result = []
dfs_ = (dfs(graph,s,visited,result))
result = []
visited = [False] * (v+1)
bfs_ = (bfs(graph,s,visited,result))

for i in dfs_:
    print(i, end= " ")
print()

for i in bfs_:
    print(i, end= " ")