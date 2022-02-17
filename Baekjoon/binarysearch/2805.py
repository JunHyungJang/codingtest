import copy

n,m = map(int,input().split())

tree = list(map(int,input().split()))
# k = len(tree) // 2
max_tree = max(tree)
start = 0
end = max_tree
def binary(tree,start, end):
    result = 0
    # print(result)

    mid = (start +end)//2
    for i in tree:
        wood = i-mid
        if wood < 0 :
            pass
        else:
            result += wood
    # print(result)
    # print(start, end ,mid ,result, "start", "end", "mid")
 
    if start > end:
        return end    
    if result ==m:
        return mid  

    if result < m:
        end = mid -1
    else:
        start = mid +1
    
    return binary(tree,start,end)

print(binary(tree,start,end))