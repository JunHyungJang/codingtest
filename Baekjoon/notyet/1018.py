import sys

n,m = map(int,input().split())

check = [[1]*m for i in range(n)]

chess = []
for i in range(n):
    k = list(input())
    chess.append(k)

s = chess[0][0]

for i in range(m):
    for j in range(n):
