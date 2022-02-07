import sys
input = sys.stdin.readline

def terr():
    n = int(input())
    answer = []
    for i in range(n):
        check = 0
        
        k = list(map(int,input().split()))
        number = k[0]
        army = k[1:]
        army_dict = dict()
        for i in army:
            if i in army_dict:
                army_dict[i]+=1
            else:
                army_dict[i] =1
        for key in army_dict.keys():
            if army_dict[key]/number > 0.5:
                answer.append(key)
                check+=1
                break
        if check ==0:
            answer.append("SYJKGW")
        # print(answer)
    
    for i in answer:
        print(i)

terr()