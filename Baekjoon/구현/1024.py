n,l = map(int,input().split())

def sum(k):
    return int(k**2/2 + k/2)


start = 0
end = l

answer = 10000
while True:
    for i in range(end):
        if (end-i) < l:
            break
        t = sum(end) - sum(i)
        print(t)
        if t == l:
            if answer > n:
                answer = n

    end -= 1
    
    if end - start < l:
        break

print(answer)