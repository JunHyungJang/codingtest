
# room = []

# lst = []
# n = int(input())

# for i in range(n):
#     a,b = map(int,input().split())
#     lst.append([a,b])

# lst.sort(key = lambda x : x[1])

# room.append(lst[0])
# lst.remove(lst[0])

# check = 0

# for a in lst:
#     for b in room:
#         if b[-1]<=a[0]:
#             b.extend(a)
#             check+=1
#             break
#     if check==0:
#         room.append(a)

# print(len(room))
        

import heapq

room = []

lst = []
n = int(input())

for i in range(n):
    a,b = map(int,input().split())
    lst.append([a,b])

lst.sort(key = lambda x : x[0])

heapq.heappush(room, lst[0][1])

for i in range(1,n):
    if room[0] > lst[i][0]:
        heapq.heappush(room, lst[i][1])
    else:
        heapq.heappop(room)
        heapq.heappush(room,lst[i][1])

print(len(room))