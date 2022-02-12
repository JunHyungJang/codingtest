# c, n = map(int,input().split())
# cnlist = []
# for i in range(n):
#     a,b = map(int,input().split())
#     cnlist.append([a,b])


# k = [0 for i in range(c+101)]
# for i in range(1,c+1):
#     for j in range(n):
#         if cnlist[j][0] <= i:
            
#             k[i] = max(k[i], k[i-cnlist[j][0]] + cnlist[j][1])
        
#     if k[i] >=c:
#         print(i)
#         break


from cmath import inf


c, n = map(int,input().split())
cnlist = []
for i in range(n):
    a,b = map(int,input().split())
    cnlist.append([a,b])

k = [float('inf') for i in range(c+101)]
k[0] = 0
for i in range(1,c+101):
    for j in range(n):
        if cnlist[j][1] <= i:
            k[i] = min(k[i], k[i-cnlist[j][1]] + cnlist[j][0])
            # print(i,k[i])

print(min(k[c:c+101]))


# from cmath import inf


# c, n = map(int,input().split())
# data = []
# inf = 1e9
# min_cost = [inf] * (c+100)
