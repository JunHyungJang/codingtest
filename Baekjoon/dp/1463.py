import sys
n = int(input())

inf = sys.maxsize

dp = [inf] * (10**6+1)

dp[1] = 0
dp[2] = 1

if n <= 2:
    print(dp[n])
else:
    for i in range(3,n+1):
        left = []
        if i% 3 == 0:
            left.append(i//3)
        if i%2 == 0:
            left.append(i//2)
        if i>=2:
            left.append(i-1)
        # print(i,left)
        
        for j in left:
            dp[i] = min(dp[i], dp[j])
        dp[i]+=1


    print(dp[n])