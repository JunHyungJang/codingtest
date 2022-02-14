# not yet

n = int(input())

w = list(map(int,input().split()))
print(w)

for i in range(1,(sum(w)+1)):
    c = i
    for j in range(n):
        if c>=w[j]:
            c-=w[j]
    if c!=0:
        answer = c
        break

print(answer)   
