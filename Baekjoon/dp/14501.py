n = int(input())

lst = []

for i in range(n):
    a,b = map(int,input().split())
    lst.append([a,b])

# lst.insert(0,[0])
# print(lst)
dp = [0] * (n+1)

for i in range(n-1,-1,-1):
    if i + lst[i][0] > n:
        dp[i] = dp[i+1]
    else:
        dp[i] = max(dp[i+1], dp[i+lst[i][0]] + lst[i][1])

print(dp[0])

