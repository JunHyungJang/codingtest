import copy

n = int(input())
k = int(input())

lst = []

for i in range(n):
    lst.append((input()))

answer = ""

resultt = []
def finding(t):
    global answer
    global k
    if len(t) == k:
        if answer not in resultt:
            result = copy.deepcopy(answer)
            resultt.append(result)
            
    else:
        for i in range(len(lst)):
            if i in t:
                continue
            else:
                t.append(i)
                answer += lst[i]
                r = len(answer)
                l = len(lst[i])
                # print(t)
                finding(t)
                t.pop()
                answer = answer[:r-l]
        

finding([])

print(len(resultt))


