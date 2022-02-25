import sys

input = sys.stdin.readline
inf = sys.maxsize

n,m = map(int,input().split())


dp = [ [float('inf')] * (n) for i in range(n) ]
p = [[0] * (n) for i in range(n)]

for _ in range(m):
    a,b,c = map(int,input().split())
    dp[a-1][b-1] = min(dp[a-1][b-1],c)
    dp[b-1][a-1] = min(dp[b-1][a-1],c)
    p[a-1][b-1] = b
    p[b-1][a-1] = a







for k in range(n):
    for i in range(n):
        for j in range(n):
            if dp[i][j] > dp[i][k] + dp[k][j]:
                dp[i][j] = dp[i][k] + dp[k][j]
                p[i][j] = p[i][k]

for i in range(n):
    p[i][i] = '-'
for row in p:
    print(*row)
                