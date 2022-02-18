n = int(input())

k = [[0]* n for i in range(n)]

x = ['***','* *','***']

def star(n):
    if n == 1:
        return ["*"]
    
    stars = star(n//3)
    # print(stars, "stars")
    L = []
    

    for i in stars:
        L.append(i *3)
    for i in stars:
        L.append(i + " "*(n//3) + i)
    for i in stars:
        L.append(i*3)
    # print(L)
    return L

k = star(n)

for j in k:
    print(j)