N,T = map(int,input().split())

res = []
# lst = []/
for i in range(N):
    a,b,c = map(int,input().split())
    lst = []
    for j in range(c):
        lst.append(a + b*j)
    # print(lst)
    if lst[-1] < T:
        continue
    left = 0
    right = c-1
    answer = 0
    while left<=right:
        mid = (left + right) // 2
        # print(left,right)
        # print(mid)
        if lst[mid] >= T:
            answer = mid
            right = mid -1
        else:
            left = mid + 1
    res.append(lst[answer] - T)


print(min(res) if res else -1)