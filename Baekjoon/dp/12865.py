N,M = map(int,input().split())


lst = [[0,0]]
for i in range(N):
    a,b = map(int,input().split())
    lst.append([a,b])

dp = [[0 for i in range(M+1)] for i in range(N+1)]
print(dp)

for i in range(1,N+1):
    for j in range(1,M+1):
        a,b = lst[i]
        print(a,b)
        if j>=a:
            dp[i][j] = max(dp[i-1][j-a] + b, dp[i-1][j])
        else:
            dp[i][j] = dp[i-1][j]

# print(dp[N][M])
print(dp)