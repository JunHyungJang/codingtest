k = list(map(int,input().split()))

answer = 0
for i in k:
    answer+= i **2

print(answer%10)