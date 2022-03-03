a,b = map(int,input().split())

c = b*a

k = list(map(int,input().split()))

for i in k:
    print(int(i-c), end = " ")