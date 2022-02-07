n, score, num = map(int, input().split())

if n == 0:
    print(1)
else:
    score_list = list(map(int,input().split()))
    if n == num and score_list[-1]>=score:
        print(-1)
    else:
        res = n+1
        for i in range(n):
            if score_list[i] <= score:
                res = i+1
                break
        print(res)
# if n ==0 :
#     print(1)
# else :
#     score_list = list(map(int,input().split()))
#     score_list.sort(reverse = True)


# insertion = 0

# if len(score_list) == 0:
#     insertion +=1    
#     score_list.append(score)
# elif len(score_list) < num:
#     for i in range(len(score_list)):
#         if score > score_list[i]:
#             score_list.insert(i,score)
#             insertion +=1
#         if insertion == 1:
#             break

# else:
#     for i in range(len(score_list)):
#         if score> score_list[i]:
#             del score_list[len(score_list)-1]
#             score_list.insert(i,score)
#             insertion +=1
#         if insertion == 1:
#             break
# if insertion == 0:
#     print(-1)
# else :
#     cnt = score_list.count(score)
#     if cnt == 1:
#         print(score_list.index(score)+1)
#     else:
#         index_list = []
#         for i, value in enumerate(score_list):
#             if value == score:
#                 index_list.append(i)
#         print(index_list[0]+1)
