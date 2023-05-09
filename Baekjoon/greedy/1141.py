n = int(input())

lst = []

for i in range(n):
    word = input()
    lst.append(word)

lst.sort(key=len)
print(lst)

count = 0

for i in range(n):
    for j in range(i+1,n):
        word = lst[i]
        if lst[j].index(word) == 0:
            
