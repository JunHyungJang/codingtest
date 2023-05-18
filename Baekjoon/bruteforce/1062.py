n,k = map(int,input().split())

if k < 5:
    print(-1)
    exit()

alpha = list('abcdefghijklmnopqrstuvwxyz')
delte = ['a','n','t','i','c']
for i in delte:
    alpha.remove(i)


learned = ['a','n','t','i','c']

answer = 0

def finding(cnt):
    if cnt == k:
        return
    else:
        for i in alpha:
            learned.append(i)
            finding(cnt+1)
            learned.pop()