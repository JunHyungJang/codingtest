N,M = map(int,input().split())

lst = [i for i in range(1,N+1)]


result = []
def finding(start):
    if len(result) == M:
        for i in result:
            print(i, end = " ")
        print()
        return
    
    for i in range(start,len(lst)):
        result.append(lst[i])
        finding(i+1)
        result.remove(lst[i])

finding(0)
