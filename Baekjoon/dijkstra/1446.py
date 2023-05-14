N,M = map(int,input().split())

INF = 10**9

# graph = [[] for i in range(M+1)]
graph = {}

for i in range(N):
    a,b,c = map(int,input().split())
    if b in graph:
        graph[b].append([a,c])
    else:
        graph[b] = [[a,c]]
    
p = list(graph.keys())
print(p)
p.sort()
d = [float('inf') for i in range(M+1)]
d[0] = 0

def finding():
    for i in range(1,M+1):
        if i in p:
            for j in graph[i]:
                d[i] = min(d[i-1]+1, j[1] + d[j[0]],d[i])
        else:
                d[i] = d[i-1] + 1

finding()
print(d[-1])
print(d)

