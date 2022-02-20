import sys
import heapq

input = sys.stdin.readline

n = int(input())

heap = []
for i in range(n):
    m = int(input())
    if m == 0:
        if len(heap) == 0:
            print(0)
        else:
            k = heapq.heappop(heap)
            print(-k)
    else:
        heapq.heappush(heap,(-m))