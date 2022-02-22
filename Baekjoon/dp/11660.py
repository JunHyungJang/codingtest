import copy, sys
N, M = map(int, input().split())

#원래 매트릭스 받기
matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]


#i, j까지 sum한 매트릭스 따로 만들어주기 
sum_matrix = copy.deepcopy(matrix)
for i in range(N):
    for j in range(N):
        if i == 0 and j == 0:
            pass
        elif i == 0:
            sum_matrix[0][j] += sum_matrix[0][j-1]
        elif j == 0:
            sum_matrix[i][0] += sum_matrix[i-1][0]
        else:
            sum_matrix[i][j] += sum_matrix[i-1][j] + sum(matrix[i][:j])


#예외 처리(i-2, j-2가 안되는 경우) 해주고 정답 출력
for _ in range(M):
    i, j, x, y = map(int, sys.stdin.readline().split())

    if i == 1 and j == 1:
        print(sum_matrix[x-1][y-1])
    elif i == 1:
        print(sum_matrix[x-1][y-1] - sum_matrix[x-1][j-2])
    elif j == 1:
        print(sum_matrix[x-1][y-1] - sum_matrix[i-2][y-1])
    else:
        print(sum_matrix[x-1][y-1] - sum_matrix[i-2][y-1] - sum_matrix[x-1][j-2] + sum_matrix[i-2][j-2])