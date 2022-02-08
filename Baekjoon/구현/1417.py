num = int(input())
repre = []
for i in range(num):
    k = int(input())
    repre.append(k)

others = repre[1:]
ticket = 0
if num == 1:
    print(0)
else:
    while max(others)>= repre[0]:
        data = others.index(max(others))
        repre[0]+=1
        others[data]-=1
        ticket+=1
    print(ticket)
    
    
    
    
    
    
    
    
    
        # while 1:
    #     check = 0
    #     for i in range(1,num):
    #         if repre[0] > repre[i]:
    #             check+=1
    #     if check == num-1:
    #         print(ticket)
    #         break
    #     for i in range(1,num):
    #         if repre[0] > repre[i]:
    #             pass
    #         else:
    #             repre[0]+=1
    #             repre[i]-=1
    #             ticket+=1
    #             # print(repre, i)
            