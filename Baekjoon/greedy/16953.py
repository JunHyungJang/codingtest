import sys

inf = sys.maxsize

answer = inf

n,m = map(int,input().split())


def finding(n,k):
    global answer
    global m
    # print(n,k,m)
    if n > m:
        return
    
    if n == m:
        answer = min(answer,k+1)
        return
    
    if 10*n+1 <= m:
        finding(10*n+1,k+1)
    
    if 2*n <=m:
        finding(2*n, k+1)

finding(n,0)

if answer == inf:
    print(-1)
else:
    print(answer)