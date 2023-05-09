c,a,b = map(int,input().split())

print(a,b,c)

lst = [0] * c

lst[a-1] = 1
lst[b-1] = 1
count = 0

new_list = []

a = True
count = 0

while a:
    count +=1
    for i in range(int((len(lst))/2)):
        p1 = lst[2*i]
        p2 = lst[2*i+1]
        if p1==p2 and p1 ==1:
            a = False
        elif p1 > p2 :
            new_list.append(p1)
        else:
            new_list.append(p2)
    lst = new_list
    new_list = []

print(count)

#answer

# n,start,end=map(int, input().split())
# cnt=0
# while start!=end:
#   start -= start//2
#   end -= end//2
#   cnt+=1
# print(cnt)