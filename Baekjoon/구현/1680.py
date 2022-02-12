k = int(input())

for i in range(k):
    w, n = map(int,input().split())
    xlist = []
    wlist = []
    for j in range(n):
        x_i, w_i = map(int,input().split())
        xlist.append(x_i)
        wlist.append(w_i)
    result = 0
    total = 0
    print(xlist, wlist)
    check = 0
    while check!= n:
        total+=wlist[check]
        if check != 0:
            result+=xlist[check] - xlist[check-1]
        else:
            result+=xlist[check]
        
        if total<w:
            check+=1
            if check == n-1:
                result+=xlist[check]
                check+=1
        else:
            total = 0
            result+=xlist[check]
        print(result)

