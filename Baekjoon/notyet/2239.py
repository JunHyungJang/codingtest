# 시간초과 not yet

import sys

input = sys.stdin.readline


lst = []
p = []
for i in range(9):
    k = list(map(int,input().rstrip()))
    p.append(k)
    for j in range(9):
        if k[j] == 0:
            lst.append([i,j])





def finding(t):
    if t == len(lst):
        # print("answer")
        for i in range(9):
            for j in range(9):
                print(p[i][j], end = "")
            print()
        exit(0)

    x,y = lst[t]
    for num in range(1,10):
      if square(x,y,num) and hori(x,y,num) and vert(x,y,num):
          p[x][y] = num
          finding(t+1)
          p[x][y] = 0

def square(x,y,k):
    cx = x//3
    cy = y//3

    for i in range(3):
        for j in range(3):
            if cx*3+i == x and cx*3+j == y:
                continue
            if p[cx*3+i][cy*3+j] == k:
                return False
    
    return True

def hori(x,y,k):
    for i in range(9):
        if p[x][i] == k:
            return False
    return True

def vert(x,y,k):
    for i in range(9):
        if p[i][y] == k:
            return False
    return True

finding(0)