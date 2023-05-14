N,M = map(int,input().split())

lst = [i for i in range(1,N+1)]


result = []

def finding(start):
    if len(result) == M:
        for i in result:
            print(i, end =" ")
        print()
    else:
        for i in range(len(lst)):
            if len(result) > 0:
                if lst[i] >= result[-1]:        
                    result.append(lst[i])
                    finding(i+1)    
                    result.pop()    
            else:
                result.append(lst[i])
                finding(i+1)
                result.pop()

finding(0)