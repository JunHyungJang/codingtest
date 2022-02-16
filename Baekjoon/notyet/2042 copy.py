n,m,k = map(int,input().split())

nlist = []
for i in range(n):
    t = int(input())
    nlist.append(t)


tree = [0] * 15


def init(node,start,end):
    if start == end :
        tree[node] = nlist[start]
        return tree[node]
    else :
        # 재귀함수를 이용하여 왼쪽 자식과 오른쪽 자식 트리를 만들고 합을 저장.
        tree[node] = init(node*2, start, (start+end)//2) + init(node*2+1, (start+end)//2+1, end)
        return tree[node]


init(1,0,n-1)

print(tree)
