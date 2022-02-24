import sys


import sys
import heapq

input = sys.stdin.readline

n = int(input())

room = []
for i in range(n):
    a,b,c = map(int,input().split())
    room.append([b,c])

q = []

room.sort()

heapq.heappush(q, room[0][1])
# print(room)
# print(room)

for i in range(1,n):
    # print(q) 
    if q[0] <= room[i][0]:
        heapq.heappop(q)
        heapq.heappush(q,room[i][1])
    else:
        heapq.heappush(q,room[i][1])

print(len(q))
