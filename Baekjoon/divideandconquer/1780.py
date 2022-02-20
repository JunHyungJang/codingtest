
def cut(x,y,n):
    global minusone, zero, plusone

    check = paper[x][y]

    for i in range(x,x+n):
        for j in range(y,y+n):
            if paper[i][j] != check:
                for a in range(3):
                    for b in range(3):
                        cut(x+n//3*a,y+n//3*b,n//3)
                return 
    if check == -1:
        minusone+=1
    elif check == 0:
        zero+=1
    elif check == 1:
        plusone+=1
    
    # print(minusone)

n = int(input())

paper = []

minusone = 0
zero = 0
plusone = 0

for i in range(n):
    k = list(map(int,input().split()))
    paper.append(k)
# print(paper)
cut(0,0,n)
print(minusone)
print(zero)
print(plusone)
