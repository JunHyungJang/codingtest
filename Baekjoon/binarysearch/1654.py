K, N = map(int,input().split())

# for i in range(K):

# print(805//100)

lst = []

for i in range(K):
    k = int(input())
    lst.append(k)

left = 1
right = max(lst)
res = 0
def finding(mid):
    answer = 0
    for i in lst:
        k = (i//mid)
        answer+=k
    return answer
# print(k,"k")
# print(left,right)
# print(K)
while left<=right:
    mid = (left + right) // 2
    result = finding(mid)

    # print(result,mid)



    if result >=N :
        # print("up")
        left = mid+1
        res = mid
    else:
        right = mid - 1

print(res)


