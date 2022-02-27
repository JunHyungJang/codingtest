from collections import deque
import sys
input = sys.stdin.readline

n = int(input())

for i in range(n):
    a,b = map(int,input().split())
    q = deque()
    lst = list(map(int,input().split()))
    for j in range(a):
        q.append((lst[j], j))
    
    # check = set(lst)
    check = lst
    check.sort()
    num = 0
    while 1:
        c,d = q.popleft()

        if c>= check[-1]:
            num+=1
            check.pop()
            if b == d:
                print(num)
                break
        else:
            q.append((c,d))
