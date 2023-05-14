N = int(input())

lst = []
for i in range(N):
    lst.append(int(input()))

total = 0
lst.sort(reverse = True)
i = 0
while i <= len(lst) -1:
    # print(total)
    if i == len(lst) - 1:
        total+=lst[i]
        break

    else:
        if lst[i] * lst[i+1] >= lst[i] + lst[i+1]:
            total+= lst[i] * lst[i+1]
            i+=2
        else:
            total+=lst[i]
            i+=1

print(total)