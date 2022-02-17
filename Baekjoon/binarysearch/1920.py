def binary_search(data,start,end,target):
    if start > end:
        return 0
    mid = (start+end) // 2
    # print(data)
    if data[mid] == target:
        return 1
    elif data[mid] > target:
        end = mid - 1
    else:
        start = mid + 1
    
    return binary_search(data, start, end ,target)


n = int(input())

data = list(map(int,input().split()))
data.sort()
# print(data)
m = int(input())

t = list(map(int,input().split()))

# print(data)


start =0
end = len(data)-1


for i in t:
    print(binary_search(data,start,end, i))

