import heapq
import sys

input = sys.stdin.readline

n = int(input())

q=  []

for i in range(n):
    k = int(input())

    if k!=0 :
        heapq.heappush(q,(abs(k),k))
    elif k == 0:
        if len(q) == 0:
            print(0)
        else:
            a,b = heapq.heappop(q)
            print(b)