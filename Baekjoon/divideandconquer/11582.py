from re import L


n = int(input())

chicken = list(map(int,input().split()))

check = int(input())

answer = []

def finding(k):
    global check
    if len(k) <=1:
        return k
    mid = len(k) // 2

    leftlist = k[:mid]
    rightlist = k[mid:]
    
    left = finding(leftlist)
    right = finding(rightlist)
    
    if len(left) == len(chicken)//check:
        answer.extend(left)
        answer.extend(right)
    if len(answer) == len(chicken):
        # print(answer)
        return answer
    return merge(left,right)

def merge(left,right):
    result = []
    l = 0
    r = 0

    while l<len(left) and r<len(right) :
        if left[l]<= right[r]:
            result.append(left[l])
            l+=1
        else:
            result.append(right[r])
            r+=1
    
    if r== len(right):
        result+= left[l:]
    if l == len(left):
        result+= right[r:]
    
    # print(result)
    return result


ttt = (finding(chicken))

for i in ttt:
    print(i, end = " ")


