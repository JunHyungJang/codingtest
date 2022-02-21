n = int(input())

card = list(map(int,input().split()))

num = [0]* (n+1)
card.insert(0,0)
# print(card)

for i in range(1,n+1):
    for j in range(1,len(card)+1):
        if j<=i:
            num[i] = max(num[i], num[i-j] + card[j])

print(num[n])




