import sys
inf = sys.maxsize

n,m = input().split()

result = inf

c = 1 + len(m)- len(n)

for i in range(c):
    t = 0
    for j in range(len(n)):
        if n[j] != m[i+j]:
            t+=1
    result = min(t,result)

print(result)   
