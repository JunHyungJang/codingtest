n,m = map(int,input().split())

A = list(map(int,input().split()))
B = list(map(int,input().split()))


    
def finding(a,b):
    i = 0
    j = 0
    answer = []
    while i != (len(a)) and j != (len(b)):
        # print(i,j)
        if a[i] <= b[j]:
            answer.append(a[i])
            i+=1
        elif a[i] > b[j]:
            answer.append(b[j])
            j+=1
        # print(answer
    # print(i,j)
    if i != (len(a)):
        answer.extend(a[i:])
    if j != (len(b)):
        answer.extend(b[j:])
    
    return answer


k = (finding(A,B))

for i in k:
    print(i, end = " ")