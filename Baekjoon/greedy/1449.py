a,b = map(int,input().split())

hole = list(map(int,input().split()))
hole.sort()


k = hole[0]
answer = 1

for i in range(1,a):
    # print(hole[i])
    if hole[i]+0.5<= k-0.5+b:
        continue
    
    elif hole[i] +0.5 > k-0.5+b:
        k = hole[i]
        answer+=1
print(answer)
