n = int(input())


count = 0

arr = []
for i in range(n):
    a,b = map(int,input().split())
    arr.append([b,a])

arr.sort(reverse = True)

# time = lst[-1][0]

# print(lst)


ans = arr[0][0] - arr[0][1]
for i in range(1,n):
    if ans > arr[i][0]:
        ans = arr[i][0] - arr[i][1]
    else:
        ans -= arr[i][1]

print(ans if ans>=0 else -1)


# for i in range(n):
#     if i == 0:
#         time -= lst[n-1-i][1]
#     else:
#         if i == 4:
#             if (time - lst[n-1-i][1]) < 0 or (lst[n-1-i][0] - lst[n-1-i][1]) <0 :
#                 print(-1)
#                 break
#         else:
#             if (time - lst[n-1-i][1]) < lst[n-2-i][0] or (lst[n-1-i][0] - lst[n-1-i][1]) <0 :

                      
#         if time > lst[n-1-i][1]:
#             time = lst[n-1-i][0] - lst[n-1-i][1] 
#         else:
#             time -= lst[n-1-i][1]

# print(time)