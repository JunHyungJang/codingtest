import sys
input = sys.stdin.readline
number = int(input())
answer = list(map(int,input().split()))

line = [0 for i in range(number)]
    # print(line)

for i in range(number):
    count = 0
    for j in range(number):
        if line[j] == 0:
            count+=1
        if count == answer[i]+1:
            line[j] = i+1
            break
    # print(line)

for i in line:
    print(i, end = " ")
    




# random sorting
# import random
# import sys

# input = sys.stdin.readline
# number = int(input())
# answer = list(map(int,input().split()))


# def line(): 
#     check = 0
#     while 1 :
#         check = 0
#         rlist = [ i for i in range(1,number+1)]
#         random.shuffle(rlist)
#         # print(rlist)
#         # print(rlist)

#         for i in range(number):
#             count = 0
#             # print(rlist[i], "rlist i")
#             for j in range(0,i):
#                 if rlist[j]>rlist[i]:
#                     count+=1
#             # print(count)
#             # k = answer[answer.index(rlist[i])]
#             k = answer[rlist[i]-1]
#             if k == count:
#                 check+=1
#         if check == number:
#             return rlist

# print(line())

