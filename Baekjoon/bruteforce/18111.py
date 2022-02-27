from copy import deepcopy
import sys

input = sys.stdin.readline


n,m,b = map(int,input().split())

graph = []

s = 0
for i in range(n):
    k = list(map(int,input().split()))
    s+=sum(k)
    graph.append(k)


# print(bound)

time = sys.maxsize
height = 0 

for i in range(257):
    bot = top = 0
    block  = b
    for j in range(n):
        for k in range(m):
            if graph[j][k] < i:
                top += i - graph[j][k]
            else:
                bot += graph[j][k] -i

    if top > bot + b:
        continue
    t = top + bot * 2
    if t<= time:
        time = t
        height = i

print(time, height)
        

# print(answer)
# print(min(answer), answer.index(min(answer)))
