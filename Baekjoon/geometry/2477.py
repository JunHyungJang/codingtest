k = int(input())

hor = []
ver = []

for i in range(6):
    a,b = map(int,input().split())
    # print(a,b)
    if a == 1 or a== 2:
        hor.append([a,b])
    elif a == 3 or a== 4:
        ver.append([a,b])
# print(hor,ver)
hor.sort(key = lambda x : -x[1])
ver.sort(key = lambda x : -x[1])
maxhor = hor[0][1]
maxver = ver[0][1]

marhor = hor[0][1]- hor[1][1]
marver = ver[0][1]  - ver[1][1]
# print(hor,ver)


# print(marhor,marver)
result = maxhor * maxver - (marhor*marver)

answer = result * k

print(answer)