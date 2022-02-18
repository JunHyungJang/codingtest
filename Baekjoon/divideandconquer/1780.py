# n = int(input())

# paper = []

# minusone = 0
# zero = 0
# plusone = 0

# for i in range(n):
#     k = list(map(int,input().split()))
#     paper.append(k)

# def finding(paper):
#     global minusone
#     global zero
#     global plusone

#     if len(paper) == 1:
#         if paper[0] == 0:
#             zero+=1
#         elif paper[0] == 1:
#             plusone+=1
#         else:
#             minusone+=1
#     else:
#         p = len(paper)//3
#         first = paper[0:p][:]

#         second = paper[p:2*p][:]
#         third = paper[2*p:][:]
n = int(input())

paper = []
for i in range(n):
    k = list(map(int,input().split()))
    paper.append(k)

p = n
first = paper[0:p][:]
second = paper[p:2*p][:]
third = paper[2*p:][:]
fourth = paper[0][0:3]
print(fourth)