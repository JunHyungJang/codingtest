from collections import deque

n = int(input())
t = int(input())
dp = [[] for i in range(n+1)]
# print(dp)
visited = [False] *(n+1)


for i in range(t):
    a,b = map(int,input().split())
    dp[a].append(b)
    dp[b].append(a)


answer = 0
visited[1] = True


def bfs(i):
    global answer
    
    q = deque()
    q.append(i)

    while q:
        a = q.popleft()

        for i in dp[a]:
            if not visited[i]:
                visited[i] = True
                q.append(i)
                answer+=1

bfs(1)
print(answer)
