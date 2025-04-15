# https://www.acmicpc.net/problem/2578
# 빙고 백준 2578

arr = [list(map(int, input().split())) for _ in range(5)]
number = [list(map(int, input().split())) for _ in range(5)]

visited = [[0] * 5 for _ in range(5)]
answer = 0

def find_number(num):
    for y in range(5):
        for x in range(5):
            if arr[y][x] == num:
                return y, x

def check_bingo():
    cnt = 0
    # 가로 빙고 확인
    for y in range(5):
        tmp_cnt = 0
        for x in range(5):
            if visited[y][x] == 1:
                tmp_cnt += 1
            else:
                break
        if tmp_cnt == 5:
            cnt += 1
    # 세로 빙고 확인
    for x in range(5):
        tmp_cnt = 0
        for y in range(5):
            if visited[y][x] == 1:
                tmp_cnt += 1
            else:
                break
        if tmp_cnt == 5:
            cnt += 1
    # 대각선 빙고 확인
    tmp_cnt = 0
    for idx in range(5):
        if visited[idx][idx] == 1:
            tmp_cnt += 1
    if tmp_cnt == 5:
        cnt += 1

    tmp_cnt = 0
    for idx in range(5):
        if visited[idx][4 - idx] == 1:
            tmp_cnt += 1
    if tmp_cnt == 5:
        cnt += 1

    return True if cnt >= 3 else False

for i in range(5):
    flag = 0
    for j in range(5):
        tmp_y, tmp_x = find_number(number[i][j])
        visited[tmp_y][tmp_x] = 1
        answer += 1
        if check_bingo():
            flag = 1
            break
    if flag == 1:
        break

print(answer)