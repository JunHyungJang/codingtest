n,m,k = map(int,input().split())

nlist = []
for i in range(n):
    t = int(input())
    nlist.append(t)


tree = [0] * n * 4


def init(node,start,end):
    if start == end :
        tree[node] = nlist[start]
        return tree[node]
    else :
        # 재귀함수를 이용하여 왼쪽 자식과 오른쪽 자식 트리를 만들고 합을 저장.
        tree[node] = init(node*2, start, (start+end)//2) + init(node*2+1, (start+end)//2+1, end)
        return tree[node]

def subsum(node,start,end,left,right):
    if left > end or right < start:
        return 0
    
    if left<= start and end <= right:
        return tree[node]
    
    return subsum(node*2,start,(start+end)//2,left,right) + subsum(node*2+1, (start+end)//2+1,end,left,right)

def update(node,start,end,index,diff):
    if index< start or index > end:
        return
    tree[node] +=diff

    if start!=end :
        update(node*2, start, (start+end)//2, index, diff)
        update(node*2+1, (start+end)//2+1, end, index, diff)


init(1,0,n-1)


for i in range(m+k):
    a,b,c = map(int,input().split())

    if a == 1:
        b = b-1
        diff = c - nlist[b]
        nlist[b] = c
        update(1,0,n-1,b,diff)
    elif a== 2:
        print(subsum(1,0,n-1,b-1,c-1))
