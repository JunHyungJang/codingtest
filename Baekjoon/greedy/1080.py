n,m = map(int,input().split())

q = []
answer = []
for i in range(n):
    k = list(map(int,input()))
    q.append(k)
for j in range(n):
    k = list(map(int,input()))
    answer.append(k)


def reverser(x,y):
    for i in range(x,x+3):
        for j in range(y,y+3):
            # print(i,j)
            q[i][j] = 1 - q[i][j]
# print(q)
count = 0

for i in range(n-2):
    for j in range(m-2):
        # print(i,j)
        if q[i][j] != answer[i][j]:
            reverser(i,j)
            count +=1 
if q == answer:
    print(count)
else:
    print(-1)