# https://www.acmicpc.net/problem/21608
# 백준 21608 상어 초등학교
from unicodedata import lookup

# 1 비어있는 칸 중에서 '좋아하는 학생이 인접한 칸에 가장 많은 칸'으로 자리를 정한다.
# 1을 만족하는 칸이 여러 개이면, 인접한 칸 중에서 '비어있는 칸이 가장 많은 칸'으로 자리를 정한다.
# 2를 만족하는 칸도 여러 개인 경우에는 '행의 번호가 가장 작은 칸', '열의 번호가 가장 작은 칸'으로 자리를 정한다.

n = int(input())    # n x n
arr = [[-1] * (n + 2)] + [[-1] + [0] * n + [-1] for _ in range(n)] + [[-1] * (n + 2)]
student = [list(map(int, input().split())) for _ in range(n * n)]
lookup_student = [[0] * 5] + sorted(student)

# 상좌우하
dy = [-1, 0, 0, 1]
dx = [0, -1, 1, 0]

# 전체 순회 - 빈자리 / 좋아하는 사람 cnt, 공백 cnt, 좌측 상단 -> 자리 잡기
for s in student:
    love_max = empty_max = -1
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            # 4방향, love_cnt, empty_cnt
            if arr[i][j] > 0:   # 빈 자리가 아니면 넘어감
                continue
            love_cnt = empty_cnt = 0
            for dr in range(4):
                ny, nx = i + dy[dr], j + dx[dr]
                if arr[ny][nx] in s[1:]:    # 주변에 좋아하는 친구 있으면
                    love_cnt += 1
                if arr[ny][nx] == 0:    # 빈칸인 경우
                    empty_cnt += 1
            if love_max < love_cnt or love_max == love_cnt and empty_max < empty_cnt:
                love_max, empty_max = love_cnt, empty_cnt
                ei, ej = i, j

    arr[ei][ej] = s[0] # 모든 위치 체크한 후 최종 자리에 번호 저장

# 학생의 만족도의 총 합
# 인접한 칸에 앉은 좋아하는 학생의 수
# 값이 0이면 학생의 만족도는 0, 1이면 1, 2이면 10, 3이면 100, 4이면 1000
table = [0, 1, 10, 100, 1000]
answer = 0
for i in range(1, n + 1):
    for j in range(1, n + 1):
        cnt = 0
        for dr in range(4):
            ni, nj = i + dy[dr], j + dx[dr]
            if arr[ni][nj] in lookup_student[arr[i][j]]:
                cnt += 1
        answer += table[cnt]

print(answer)