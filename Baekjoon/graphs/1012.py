import sys

sys.setrecursionlimit(10000)



def neighbor(w):
    up = [w[0], w[1]+1]
    down = [w[0], w[1]-1]
    right = [w[0]+1, w[1]]
    left = [w[0]-1, w[1]]
    return up,down,right,left



def dfs(w,land,m,n):
    land[w[0]][w[1]] = 2
    for k in neighbor(w):
        if k[0] > n-1 or k[1] > m-1 or k[0] <-1 or k[1] <-1 :
            pass
        else:
            if land[k[0]][k[1]] == 1:
                dfs(k,land,m,n)
    print(land,"dfs")

    

n = int(input())

for i in range(n):
    m,n,k = map(int,input().split())
    land = [[0] * m for i in range(n)]
    vege = []
    result = 0

    for j in range(k):
        a,b = map(int,input().split())
        vege.append([b,a])
        land[b][a] = 1

    for k in range(len(vege)):
        if land[vege[k][0]][vege[k][1]] == 0 or land[vege[k][0]][vege[k][1]] ==2:
            
            pass
        else:
         
            dfs([vege[k][0],vege[k][1]], land,m,n)
            result+=1

    # for i in range(n):
    #     for j in range(m):
    #         if land[i][j] > 0:
    #             dfs([i,j], land, m,n)
    #             result+=1
    

    print(result)



