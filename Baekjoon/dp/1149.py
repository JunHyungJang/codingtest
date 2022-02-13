n = int(input())

color = []

for i in range(n):
    a,b,c = map(int,input().split())
    color.append([a,b,c])

for i in range(1,n):
    color[i][0] = min(color[i-1][1], color[i-1][2]) +color[i][0]
    color[i][1] = min(color[i-1][0], color[i-1][2]) + color[i][1]
    color[i][2] = min(color[i-1][0], color[i-1][1]) + color[i][2]

print(min(color[i][0], color[i][1], color[i][2]))
