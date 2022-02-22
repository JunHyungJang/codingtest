import sys

input = sys.stdin.readline

n,m = map(int,input().split())

# n = 개수, k = 용량

k = [ [0]*(n+1) for i in range(m+1) ]

lst = []

for i in range(n):
    w,v, = map(int,input().split())
    lst.append([w,v])

#용량에 대해
for x in range(1,m+1):
    #개수에 대해 
    for j in range(1,n+1):
        k[x][j] = k[x][j-1]
        if lst[j-1][0] <= x:
            k[x][j] = max(k[x][j], k[x-lst[j-1][0]][j-1]  + lst[j-1][1])

print(k[m][n])
