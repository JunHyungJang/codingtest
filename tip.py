# input 받기
n, score, num = map(int, input().split())
score_list = list(map(int,input().split()))

# index 찾기
score_list.index(score)

# list중복된값찾기
cnt = score_list.count(score)

# list삭제
del score_list[len(score_list)-1]

# math, combinatino, factorial
result = math.factorial(b)/ (math.factorial(a) * math.factorial(b-a))
product = []
a = combinations(product, 2)

# set 
add, update, remove
frest = set()
a = [1,2,3]
frest.update(a)
print(frest)

# dfs bfs

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

# deque

q.append(item) # right
q.appendleft(item) # left
q = deque()
q.popleft()


# 다익스트라
def dijkstra(s):
    heap = []
    heapq.heappush(heap,(0,s))

    while heap:
        w, node = heapq.heappop(heap)

        if dp[node] < w:
            continue
        
        for next_node,i in graph[node]:
            print(graph[node])
            next_w = w+i
            print(next_w, next_node)
            if next_w < dp[next_node]:
                dp[next_node] = next_w
                heapq.heappush(heap,(next_w,next_node))
                
    