n = int(input())

paper = []

for i in range(n):
    k= list(map(int,input().split()))
    paper.append(k)

result0 = 0
result1 = 0

def finding(x,y,n):
    global result1, result0
    
    check = paper[x][y]

    for i in range(x,x+n):
        for j in range(y,y+n):
            if paper[i][j] != check:
                for a in range(2):
                    for b in range(2):
                        finding(x+n//2*a, y+n//2*b,n//2)
                return

    if check == 1:
        result1+=1
        # print(x,y)
        # print(result1)

    elif check == 0:
        result0+=1

finding(0,0,n)

print(result0)
print(result1)