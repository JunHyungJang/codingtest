import sys
from collections import deque

input = sys.stdin.readline

n = int(input())


def finding(a):
    q = deque()
    for j in range(len(a)):
        if a[j] == "(":
            q.append(a[j])
        elif a[j] == ")":
            if len(q) == 0:
                print("NO")
                return
            else:
                q.popleft()
    if len(q) == 0:
        print("YES")
        return
    else:
        print("NO")
        return
    

for i in range(n):
    a = input()
    finding(a)
    
