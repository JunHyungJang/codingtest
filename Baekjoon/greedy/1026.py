# n = int(input())

# a = list(map(int,input().split()))
# b = list(map(int,input().split()))

# new_a = [0] * n
# result=0

# # sortb = sorted(b,reverse= True)
# # print(sortb)
# b2 = sorted(b,reverse =True)
# a.sort()

# for i in range(n):
#     x = b.index(b2[i])
#     new_a[x] = a[i]
# # print(new_a)
    

# for i in range(n):
#     result +=new_a[i] * b[i]
# print(result)

import sys

input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

answer = 0
a.sort()
for i in range(n):
    x = a[i]
    y = b.pop(b.index(max(b)))

    answer += x * y
    
print(answer)