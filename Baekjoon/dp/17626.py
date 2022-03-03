import sys

inf = sys.maxsize
n = int(input())

dp = [0] * (n+1)

dp[0] = 0
dp[1] = 1



for i in range(2,n+1):
    
    minvalue = inf
    value = 1

    while (value**2) <= i:
        minvalue = min(minvalue, dp[i-(value**2)])
        value+=1
    
    dp[i] = minvalue+1

print(dp[n])