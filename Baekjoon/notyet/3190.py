import sys
from collections import deque

n = int(input())

graph = [[0]*n for i in range(n)]

k = int(input())

apple = []

for i in range(k):
    a,b = map(int,input().split())
    graph[a-1][b-1] = 1


t = int(input())

change = dict()

for i in range(t):
    a,b = input().split()
    change[int(a)] = b

# print(change)
# print(graph)

direction = 1
time = 0

def chdir(w,d):
    if w == "D":
        if d == 1:
            return 3
        elif d == 2:
            return 4
        elif d == 3:
            return 2
        elif d ==4:
            return 1
    elif  w == "L":
        if d==1:
            return 4
        elif d==2:
            return 3
        elif d == 3:
            return 1
        elif d ==4:
            return 2

def finding():
    global time
    global direction

    dx,dy = 0,0
    q = deque()
    while 1:
        
        time +=1

        # print(time)
        # print(q)
        
        
        if direction == 1:
            dy+=1
        elif direction == 2:
            dy-=1
        elif direction == 3:
            dx+=1
        elif direction == 4:
            dx-=1

        if time in change:
            direction = chdir(change[time], direction)
            
        
        # print(dx,dy,direction)
        # print(dx,dy,x,y)

        if 0<=dx<=n-1 and 0<=dy<=n-1:
            if (dx,dy) in q:
                return time
            
            if graph[dx][dy] == 1:
                # q.append((x,y))
                graph[dx][dy] = 0
                q.append((dx,dy))

            elif graph[dx][dy] == 0:
                q.append((dx,dy))
                a,b = q.popleft()
                
        else:
            return time

         
        
      
        

print(finding())









# not yet

# def chdirection(t,direction):
#     if t == 'D':
#         if direction == 1:
#             direction = 3
#         if direction == 2:
#             direction = 4
#         if direction == 3:
#             direction = 2
#         if direction == 4:
#             direction = 1
#     if t == "L":
#         if direction == 1:
#             direction = 4
#         if direction == 2:
#             direction = 3
#         if direction == 3:
#             direction = 1
#         if direction == 4:
#             direction = 2
    
#     return direction


# n = int(input())
# m = int(input())

# time = 0
# square = [ [0 for i in range(n)] for i in range(n)]

# for i in range(m):
#     a,b = map(int,input().split())
#     square[a-1][b-1] = 1

# k = int(input())
# chdic = dict()
# for i in range(k):
#     c,d = input().split()
#     chdic[int(c)] = d
# print(chdic)

# apple = m

# location = [0,0]
# direction = 1
# while apple !=0:
#     # print(time)
#     print(location[0], location[1], direction)

#     time+=1
#     if direction == 1:
#         location[1]+=1
#     if direction == 2:
#         location[1]-=1
#     if direction == 3:
#         location[0] +=1
#     if direction == 4:  
#         location[0] -=1

#     location[0] = a
#     location[1] = b

#     if location[0] > n-1 or location[1] >n-1 or location[0]<0 or location[1]<0 :
#         print(location[0], location[1])
#         print(time)
#         break

#     if square[a-1][b-1] == 1:
#         print(a,b)
#         print(square)
#         square[a-1][b-1] = 0
#         apple-=1
    
#     if time in chdic:
#         change = chdic[time]
#         direction = chdirection(change,direction)




