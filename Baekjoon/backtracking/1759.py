n, m = map(int,input().split())
# w = list(map(int,input().split()))
k = list(input().split())
k.sort()

answer = []
mom = ['a','e','i','o','u']

def dfs(n,k,s):
    if len(answer) == n:
        r = 0
        l = 0
        for j in answer:
            if j in mom:
                r+=1
            else:
                l+=1
        if r>=1 and l>=2:
            for i in answer:
                print(i, end="")
            print()
    else:
        for i in range(s,len(k)):
            answer.append(k[i])
            dfs(n,k,i+1)
            answer.pop()

dfs(n,k,0)    