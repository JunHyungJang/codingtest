from itertools import permutations
import math

# def fd():
#     lis = ['a','a','z','z']


# def finding():
#     n,m,k = map(int,input().split())


#     aldic = []

#     for i in range(n):
#         aldic.append('a')
#     for j in range(m):
#         aldic.append('z')

#     leng = math.factorial(n+m) / (math.factorial(m) * math.factorial(n))

#     if leng< k:
#         return -1
#     allist = (list(set(list(permutations(aldic)))))



#     allist.sort()
#     # print(allist)

#     result = allist[k-1]
#     answer = ''

#     for i in range(len(result)):
#         answer+=allist[k-1][i]
#     return answer

# print(finding())

n,m,k = map(int,input().split())

leng = math.factorial(n+m) / (math.factorial(m) * math.factorial(n))

if leng < k:
    print(-1)
else:
    while True:
        