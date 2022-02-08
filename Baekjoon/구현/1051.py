n, m = map(int,input().split())

rect = []
for i in range(n):
    k = input()
    empty = []
    for j in range(m):
        empty.append(int(k[j]))
    rect.append(empty)
# print(rect)

poss = min(n,m)

result = 1
size = 1
while poss>=size:
    for k in range(0,n-size+1):
        for j in range(0,m-size+1):
            if rect[k][j] == rect[k][j+size-1] == rect[size-1+k][j] == rect[size-1+k][j+size-1]:
                result = size
                # print(result)
            else:
                pass
    size+=1

print(result*result)
