n = int(input())

lst = [ i for i in range(0,n)]

# print(lst)

start = 2
end = 1
answer = []
while 1<=start<n and 1<=end < n and start>end:
    
    guess = lst[start]**2 - lst[end]**2
    if guess== n:
        answer.append(start)
        start+=1
    elif guess > n:
        end+=1
    else:
        start+=1


# print(answer)

if len(answer) == 0:
    print(-1)
else:
    for i in answer:
        print(i)