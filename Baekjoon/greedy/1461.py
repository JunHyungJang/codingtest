# not yet

import heapq
# from selectors import EpollSelector
n,m = map(int,input().split())



book = list(map(int,input().split()))

left = []
right = []
for i in book:
    if i>0:
        heapq.heappush(right,i)
    else:
        heapq.heappush(left,abs(i))

result = 0
while (len(left)+len(right)) != 0 :
    if len(left) >=m:
        for i in range(m):
            l = heapq.heappop(left)
        result+= l*2
    if len(right) >=m:
        for i in range(m):
            r = heapq.heappop(right)
        result+= r*2
    
    if 0<len(left)<m and len(right) == 0:
        for i in range(len(left)):
            f = heapq.heappop(left)
        result+=f
    
    if 0<len(right)<m and len(left) == 0:
        for i in range(len(right)):
            f = heapq.heappop(right)
        result+=f
    
    if 0<len(left)< m and 0<len(right)< m:
        if max(left) >= max(right):
            for i in range(len(right)):
                o = heapq.heappop(right)
            result += o*2
            for j in range(len(left)):
                f = heapq.heappop(left)
            result+= f
        else:
            for i in range(len(left)):
                o = heapq.heappop(left)
            result += o*2
            for j in range(len(right)):
                f = heapq.heappop(right)
            result+= f
    
    print(left,right)
    print(result)
print(result)


    # if len(left)< m and len(right)< m :
    #     if len(left) ==0:
    #         heapq.heappush(left,0)
    #     if len(right) ==0:
    #         heapq.heappush(right,0)
    #     print(left,right)
        # if max(left) >= max(right):
        #     for i in range(len(right)):
        #         o = heapq.heappop(right)
        #     result += o*2
        #     for j in range(len(right)):
        #         f = heapq.heappop(left)
        #         if j== len(right)-1:
        #             result+= f
        # else:
        #     for i in range(len(left)):
        #         o = heapq.heappop(left)
        #     result += o*2
        #     for j in range(len(right)):
        #         f = heapq.heappop(right)
        #     result+= f


