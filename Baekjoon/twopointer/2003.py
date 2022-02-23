import sys

input = sys.stdin.readline

n,m = map(int,input().split())

lst = list(map(int,input().split()))


i = 0
j = 0

cnt = 0

while i!=n:
    if sum(lst[i:j+1]) == m:
        cnt+=1
        i+=1
        j = i
    elif sum(lst[i:j+1]) > m:
        i+=1
    
    else:
        j+=1
        if j == n:
            i+=1
            
    # print(i,j)
print(cnt)

# import sys

# input = sys.stdin.readline

# n,m = map(int,input().split())

# lst = list(map(int,input().split()))

# start = 0
# end = 0
# count = 0

# while end < len(lst) and start<len(lst):
#     if sum(lst[start:end+1]) <m:
#         end+=1
    
#     elif sum(lst[start:end+1]) == m:
#         count+=1
#         if start<end:
#             start+=1
#         else:
#             end+=1

#     else:
#         start+=1

# print(count)
         