from operator import ilshift


n = int(input())
door = list(map(int,input().split()))
c = int(input())
# print(door)

dp = [0 for i in range(c+1)]
for i in range(1,c+1):
    for j in range(n):
        if door[j] <=i:
            dp[i] = max(dp[i], 10*dp[i-door[j]] + j )

# for i in range(len(dp)):
#     print(i, dp[i])

print(dp[-1])