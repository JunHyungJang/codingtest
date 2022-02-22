import sys

input = sys.stdin.readline

t = int(input())
for i in range(t):
    n = int(input())
    lst = []
    for j in range(n):
        a,b = map(int,input().split())
        lst.append([a,b])
    lst.sort()
    maxx = lst[0][1]
    count = 0
    for a in range(n):
        if a == 0:
            count+=1
        else:
            if maxx> lst[a][1]:
                count+=1
                maxx = lst[a][1]
    print(count)
                