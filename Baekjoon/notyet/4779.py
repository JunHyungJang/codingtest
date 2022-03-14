def finding(start,end):
    if end - start == 1:
        return
    
    x = (end-start)//3

    for i in range(start+x,end-x):
        lst[i] = " "
    
    finding(start,start+x)
    finding(end-x,end)




while 1:
    try:
        n = int(input())
        if n == "":
            break
        m = 3**n
        lst = ["-"] * m
        # print(lst)
        finding(0,m)
        for j in lst:
            print(j, end = "")
    except EOFError:
        break
    

