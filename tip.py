# input 받기
n, score, num = map(int, input().split())
score_list = list(map(int,input().split()))

# index 찾기
score_list.index(score)

# list중복된값찾기
cnt = score_list.count(score)

# list삭제
del score_list[len(score_list)-1]

