graph = []
lst = []
for i in range(9):
    k = list(map(int,input().split()))
    graph.append(k)
    for j in range(9):
        if k[j] == 0:
            lst.append([i,j])

def vert(i,j,num):
    for k in range(9):
        if graph[k][i] == num:
            return False
    
    return True


def hori(i,j,num):
    for k in range(9):
        if graph[i][k] == num:
            return False
    
    return True

def square(i,j,num):
    l = 3*(i//3)
    r = 3*(j//3)
    for x in range(l,l+3):
        for y in range(r,r+3):
            if graph[x][y] == num:
                return False
    
    return True
        
def finding(t):
    x,y = lst[t]
    if t == len(lst):
        for i in range(n):
            for j in range(n):
                print(graph[i][j], end = " ")
            print()
    else:
        for z in range(1,10):
            num = z
            if vert(x,y,num) and hori(x,y,num) and square(x,y,num):
                graph[x][y] = num
                finding(t+1)
                print(1)
                graph[x][y] = 0

finding(0)
