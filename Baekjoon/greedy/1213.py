word = list(input())

l = len(word)

lst = [0] * len(word)

dic = {}

for i in word:
    if i in dic:
        dic[i] +=1
    else:
        dic[i] = 1
dic_sort = sorted(dic.items())
# sorted(dic, reverse = True)
# print(dic_sort)



def finding():
    
    flag = 0
    t = -1
    while True:
        # for i in dic_sort:
            # x,y = i
        if (l%2) == 0:
            for i in dic_sort:
                x,y = i
                # print(x,y)
                if (y%2) !=0:
                    print("I'm Sorry Hansoo")
                    return
                else:
                    # print(y/2, "length")
                    for k in range(int(y/2)):
                        # print(flag, "flag")
                        lst[flag] = x
                        lst[l-1-flag] = x
                        flag +=1
        else:
            for i in range(int(len(dic_sort))):
                x,y = dic_sort[i]
                if (y%2) != 0:
                    if t == -1:
                        t = i
                        # print(y)
                        # print(int((y-1)/2))
                        for k in range(int((y-1)/2)):
                            lst[flag] = x
                            lst[l-1-flag] = x
                            flag +=1
                    else:
                        print("I'm Sorry Hansoo")
                        return
                else:
                    for k in range(int((y/2))):
                        lst[flag] = x
                        lst[l-1-flag] = x
                        flag +=1
        
        break
    if t!= -1:
        x,y = dic_sort[t]
        lst[int((l-1)/2)] = x
    for i in lst:
        print(i,end = "")

finding()
            

