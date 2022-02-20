import sys
sys.setrecursionlimit(10*8)
import math
n,a,b = map(int,input().split())

result = 0
def finding(x,y,n):
    global a,b
    global result

    if n == 2:
        if a % 2 == 0:
            if b % 2 == 0:
                return result
            else:
                result+=1
                return result
        else:
            if b % 2 == 0:
                result+=2
                return result
            else:
                result+=3
                return result

    for i in range(2):
        for j in range(2):
            new_x = x + i*(n//2)
            new_y = y + j*(n//2)
            if new_x <= a <= new_x + (n//2)-1 and new_y<=b<=new_y + (n//2) -1:
                # print(new_x,new_y)
                # print(result)
                finding(new_x,new_y,n//2)
                return 
            else:
             k = (n//2) **2
             result+=k
    
t = math.pow(2,n)
# print(t)
finding(0,0,t)
print(int(result))