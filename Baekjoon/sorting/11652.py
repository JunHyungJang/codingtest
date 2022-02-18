import sys

n = int(input())

numdict = {}

for i in range(n):
    k = int(input())
    if k in numdict:
        numdict[k]+=1
    else:
        numdict[k] = 1
# print(numdict.items())
numdict = sorted(numdict.items(), key = lambda x : (-x[1], x[0]))

print(numdict[0][0])

