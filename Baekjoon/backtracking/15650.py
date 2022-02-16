n,m = map(int,input().split())


s = []
t = 1
def dfs(n,m,t):
    if len(s) == m:
        for i in s:
            print(i, end = " ")
        print()
    
    else:
        for i in range(t,n+1):
            s.append(i)
            dfs(n,m,i+1)
            s.pop()

dfs(n,m,t)

