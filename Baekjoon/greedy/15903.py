import heapq

n,m = map(int,input().split())

lst = list(map(int,input().split()))
heapq.heapify(lst)

a = 0
# print(lst)
while a < m:
    x = heapq.heappop(lst)
    y = heapq.heappop(lst)
    plus = x+y
    x = plus
    y = plus
    heapq.heappush(lst,x)
    heapq.heappush(lst,y)
    # print(lst)
    a+=1

print(sum(lst))