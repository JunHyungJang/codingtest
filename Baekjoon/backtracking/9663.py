n = int(input())

chess = [0] * n

answer = 0
def dfs(x):
    global answer
    if x == n:
        answer+=1
    
    else:
        for i in range(n):
            chess[x] = i
            if checking(x):
                dfs(x+1)

def checking(x):
    for i in range(x):
        if chess[x] == chess[i] or abs(chess[x]- chess[i]) == x-i:
            return False
    return True

dfs(0)
print(answer)