# not yet

def chdirection(t,direction):
    if t == 'D':
        if direction == 1:
            direction = 3
        if direction == 2:
            direction = 4
        if direction == 3:
            direction = 2
        if direction == 4:
            direction = 1
    if t == "L":
        if direction == 1:
            direction = 4
        if direction == 2:
            direction = 3
        if direction == 3:
            direction = 1
        if direction == 4:
            direction = 2
    
    return direction


n = int(input())
m = int(input())

time = 0
square = [ [0 for i in range(n)] for i in range(n)]

for i in range(m):
    a,b = map(int,input().split())
    square[a-1][b-1] = 1

k = int(input())
chdic = dict()
for i in range(k):
    c,d = input().split()
    chdic[int(c)] = d
print(chdic)

apple = m

location = [0,0]
direction = 1
while apple !=0:
    # print(time)
    print(location[0], location[1], direction)

    time+=1
    if direction == 1:
        location[1]+=1
    if direction == 2:
        location[1]-=1
    if direction == 3:
        location[0] +=1
    if direction == 4:  
        location[0] -=1

    location[0] = a
    location[1] = b

    if location[0] > n-1 or location[1] >n-1 or location[0]<0 or location[1]<0 :
        print(location[0], location[1])
        print(time)
        break

    if square[a-1][b-1] == 1:
        print(a,b)
        print(square)
        square[a-1][b-1] = 0
        apple-=1
    
    if time in chdic:
        change = chdic[time]
        direction = chdirection(change,direction)




