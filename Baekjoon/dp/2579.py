import sys

n = int(input())

s = [0] * (n+1)
dp = [0] *(n+1)

for i in range(1,n+1):
    t = int(input())
    s[i] = t


dp[1] = s[1]
dp[2] = max(s[1]+s[2], s[0]+s[2])

for i in range(3,n+1):
    dp[i] = max(dp[i-3] + s[i-1] + s[i], dp[i-2] + s[i])

print(dp[-1])