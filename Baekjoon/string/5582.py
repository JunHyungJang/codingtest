import sys

input = sys.stdin.readline

x = input().rstrip()
y = input().rstrip()
# print(x)
# print(x[1])

c = [[0]*(len(y)+1) for i in range(len(x)+1)]
answer = 0
for i in range(1,len(x)+1):
    for j in range(1,len(y)+1):
        if x[i-1] == y[j-1]:
            c[i][j] = c[i-1][j-1]+1
            # print(x[i-1])
            # print(c[i][j])
            answer = max(answer, c[i][j])

print(answer)