x,y = map(int,input().split())

def victory(cnt,w):
    return (100*w) // cnt

# print(victory(53,47))

left = 0
right = x
res = x

z = victory(x,y)

if victory(x,y) >= 99:
    print(-1)
else:
    while left<=right:
        mid = (left+right) // 2
        if victory(x+mid,y+mid) > z:
            res = mid
            right = mid - 1
        else:
            left = mid + 1
    print(res)
    
    

