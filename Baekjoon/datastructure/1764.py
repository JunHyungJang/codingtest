import sys
input = sys.stdin.readline

n,m = map(int,input().split())

a = set()
b = set()

for i in range(n):
    a.add(input().rstrip())
for j in range(m):
    b.add(input().rstrip())

k = list(a&b)

k.sort()
# print(k, "k")
print(len(k))
for z in k:
    print(z)