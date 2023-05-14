N,M = map(int,input().split())

lst = list(map(int,input().split()))
lst.sort()
result = []
def finding():
    if len(result) == M :
        for i in result:
            print(i, end = " ")
        print()
    else:
        for i in lst:
            if i not in result:
                result.append(i)
                finding()
                result.pop()

finding()