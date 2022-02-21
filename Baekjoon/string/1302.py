n = int(input())

dic = dict()

for i in range(n):
    book = input().rstrip()
    if book in dic:
        dic[book]+=1
    else:
        dic[book] = 1

# print(dic.items())
k = sorted(dic.items(), key = lambda x : (-x[1], x[0]) )

print(k[0][0])