k = list(map(int,input().split()))

t = k[0]

des = 0
aes = 0

for i in range(len(k)-1):
    if k[i] > k[i+1]:
        des+=1
    elif k[i] < k[i+1]:
        aes +=1

if des == 7:
    print("descending")
elif aes == 7:
    print("ascending")
else:
    print("mixed")