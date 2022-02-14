n, m = map(int,input().split())

num = [i for i in range(1,n+1)]
check = []
# print(num)
def back(num,m,check):
    if len(check) == m:
        for j in check:
            print(j, end = " ")
        print()
    for i in num:
        check.append(i)
        num.remove(i)
        back(num,m,check)
        num.append(i)
        check.remove(i)
        num.sort()


back(num,m,check)