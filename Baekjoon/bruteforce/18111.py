from copy import deepcopy


n,m,b = map(int,input().split())

graph = []

s = 0
for i in range(n):
    k = list(map(int,input().split()))
    s+=sum(k)
    graph.append(k)


def checking(key):
    for i in range(n):
        for j in range(m):
            if key == graph[i][j]:
                pass
            else:
                return -1
    return key


answer = [float('inf')] * 257

bound = (s+b)//(n*m)
# print(bound)


for i in range(bound):
    time = 0
    block  = b
    graph_test = deepcopy(graph)
    for j in range(n):
        for k in range(m):
            diff = i - graph_test[j][k]
            if diff <0:
                time+=abs(diff) * 2
                block+=abs(diff)
            elif diff >0:
                time+= diff
                block-=diff
    if block >=0:
        answer[i] = time
        # print(i,block)
    else:
        answer[i] = float('inf')

# print(answer)
print(min(answer), answer.index(min(answer)))
