v,e = map(int,input().split())

edge = []

vroot = [ i for i in range(0,v+1)]
for i in range(e):
    a,b,w = map(int,input().split())
    edge.append([a,b,w])

edge.sort(key = lambda x : x[2]) # 가중치로 정렬

# 경로압축
def find(x): 
    if x!= vroot[x]:
        vroot[x] = find(vroot[x])
    return vroot[x]

answer = 0


for s,e,w in edge:
    root1 = find(s)
    root2 = find(e)
    if root1 != root2 :
        vroot[root1] = root2
        answer+=w

print(answer)