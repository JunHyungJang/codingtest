N,M = map(int,input().split())

lst = [ i for i in range(1,N+1)]

# print(lst)

result = []
def finding():
    if len(result) == M:
        for i in result:
            print(i, end = " ")
        print()
        return
    else:
        for i in lst:
            if i not in result:
                result.append(i)
                finding()
                result.remove(i)

finding()
    