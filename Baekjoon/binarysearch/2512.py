import sys

input = sys.stdin.readline

n = int(input())
money = list(map(int,input().split()))
m = int(input())

start = 0
end = max(money)

def binary(start, end , m):
    mid = (start + end) // 2
    # print(start,end, mid)
    if start > end :
        return end
    result = 0
    for i in money:
        if i > mid :
            result+=mid
        else:
            result+=i
    # print(result) 

    if result == m:
        return mid
    
    elif result > m :
        end = mid -1
    else:
        start = mid +1
    
    return binary(start,end,m)

print(binary(start,end,m))