num, min = map(int,input().split())

bottle = dict()
bottle[1] = num

total = 0
t= list(bottle.keys())[0]
k = bottle[t]
while k> min:
    t = list(bottle.keys())[0]
    if bottle[t] % 2 ==0:
        bottle[t*2] = k // 2
        del bottle[t]
    else:
        bottle[t*2] = k//2 +1
        total+= t
        # print(total)
        del bottle[t]
    # print(bottle)
    t = list(bottle.keys())[0]
    k = bottle[t]
    # print(bottle[t])

print(total)
# total = 0
# def merge(bottle, min,total):
#     total_key = 0
#     key = list(bottle.keys())[0]
#     total_key+= bottle[key]
#     if total_key == min:
#         return total
#     else:
#         key = list(bottle.keys())[0]
#         if bottle[key] % 2 == 0:
#             bottle[key*2] = bottle[key]/2
#             del bottle[key]
#         else:
#             k = bottle[key] // 2
#             bottle[key*2] = k+1
#             total+= key
#             del bottle[key]   
#     return merge(bottle,min,total)

# print(merge(bottle,min,total))
