
from collections import deque
import heapq

n = int(input())

card = []
for i in range(n):
    c = int(input())
    heapq.heappush(card,c)



answer = 0
while len(card) > 1:
    q1 = heapq.heappop(card)
    q2 = heapq.heappop(card)
    # print(q1,q2)
    k = q1+q2
    answer+= k
    heapq.heappush(card,k)

print(answer)

