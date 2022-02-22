n,m = map(int,input().split())

dp = []
for i in range(n):
    k = list(map(int,input().split()))
    dp.append(k)

for i in range(n):
    for j in range(m):
        if j == 0 and i >0:
            dp[i][j]+= dp[i-1][j]
        elif i == 0 and j>0:
            dp[i][j]+= dp[i][j-1]
        elif j >0 and i >0 :
            dp[i][j]+= max(dp[i-1][j-1], dp[i][j-1], dp[i-1][j])

print(dp[n-1][m-1])