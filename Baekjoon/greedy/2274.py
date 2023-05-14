n = int(input())

lst = []
for i in range(n):
    lst.append(int(input()))




lst.sort(reverse = True)

answer = []


for i in range(len(lst)):
    answer.append(lst[i]* (i+1))

print(max(answer))
            
          
    
