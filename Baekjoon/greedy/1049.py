n,m = map(int,input().split())

a = []
b = []


answer = 0
for i in range(m):
    x,y = map(int,input().split())
    a.append(x)
    b.append(y)
# print(min(a))
while n != 0:
    min_1 = min(b)
    min_6 = min(a)
    # print(min_1, min_6)
    if n>=6:
        if min_6 > min_1*6 :
            answer += n * min_1
            n = 0
        else :
            t = n // 6 #몫
            r = n % 6 #나머지
            n = r
            # print(t,r)
            answer += t * min_6
    else:
        if min_6 > min_1 * n:
            answer += n* min_1
            n = 0
        else:
            answer += min_6
            n = 0

print(answer)