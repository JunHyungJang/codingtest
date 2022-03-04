from collections import deque
a,b = map(int,input().split())

lst = [i for i in range(1,a+1)]
# print(lst)
q = deque(lst)
answer = []
for i in range(a):
    for j in range(b):
        t = q.popleft()
        if j == b-1:
            answer.append(t)
        else:
            q.append(t)

print("<", end = "")
for i in range(len(answer)):
    print(answer[i], end="")
    if i == len(answer)-1:
        continue
    else:
        print(",", end = " ")
print(">", end= "")