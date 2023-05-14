N = int(input())

lst = list(map(int,input().split()))

M = int(input())

answer = list(map(int,input().split()))

# answer.sort()
lst.sort()


res = []
for card in answer:
    left = 0
    right = len(lst) - 1
    num = 0
    while left<=right:
        mid = (left + right) // 2
        if lst[mid] == card:
            # print(lst[mid])
            num = 1
            break
        if lst[mid] >= card:
            right = mid - 1
        else:
            left = mid +1
    res.append(num)
# print(res)
for i in res:
    print(i, end = " ")

