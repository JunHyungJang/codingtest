import sys
from collections import deque

n,m = map(int,input().split())

ladder= dict()
snake = dict()
cnt = [0] * 101
visited = [False] * 101

for i in range(n):
    a,b = map(int,input().split())
    ladder[a] = b

for j in range(m):
    a,b = map(int,input().split())
    snake[a] = b


def bfs():
    queue = deque([1])
    visited[1] = True

    while queue:
        now = queue.popleft()
        for i in range(1,7):
            next = now + i
            if 0< next<=100:
                if next in ladder:
                    next = ladder[next]
                if next in snake:
                    next = snake[next]


# def finding(count, start):
#     for i in range(start,start+6):
#         if count > cnt[i]:
#             if i == start+5:
#                 count = cnt[i]
#             else:
#                 count = cnt[i]+1
#             continue
#         if i in ladder:
#             cnt[ladder[i]] = min(cnt[ladder[i]], count)
#         if i in snake:
#             cnt[snake[i]] = min(cnt[snake[i]], count)
#         cnt[i] = min(cnt[i], count)

#         if i == 100:
#             return

#     finding(count+1,start+6)

# # print(ladder, snake)

# finding(1,1)
# # print(cnt)
# print(len(cnt))
# print(cnt[100])
