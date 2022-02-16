def back(p,t):
    global lmax
    if 0 not in lineup:
        lmax = max(lmax,sum(lineup))
    else:
        for i in range(11):
            # print(lineup)
            if p[t][i] != 0 and lineup[i] == 0:
                lineup[i] = p[t][i]
                # print(lineup[i], i, t)
                t+=1
                back(p,t)
                t-=1
                lineup[i] =0


n = int(input())

for i in range(n):
    p = []
    for i in range(11):
        k = list(map(int,input().split()))
        p.append(k)
    lmax = 0
    lineup = [0] * 11
    t = 0
    # print(p)
    back(p,t)
    print(lmax)

