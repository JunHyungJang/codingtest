N = int(input())

road = list(map(int,input().split()))
gas = list(map(int,input().split()))

min_cost = gas[0]

total = road[0]* gas[0]

for i in range(1,N-1):
    if min_cost > gas[i]:
        min_cost = gas[i]
    total += road[i] * min_cost

print(total)