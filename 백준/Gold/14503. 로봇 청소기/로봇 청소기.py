# https://www.acmicpc.net/problem/14503
# 14503 백준 로봇청소기

# 현재 칸이 아직 청소되지 않은 경우, 현재 칸을 청소한다.
# 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 없는 경우,
# 바라보는 방향을 유지한 채로 한 칸 후진할 수 있다면 한 칸 후진하고 1번으로 돌아간다.
# 바라보는 방향의 뒤쪽 칸이 벽이라 후진할 수 없다면 작동을 멈춘다.
# 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 있는 경우,
# `반시계 방향`으로 90도 회전한다.
# 바라보는 방향을 기준으로 앞쪽 칸이 청소되지 않은 빈 칸인 경우 한 칸 전진한다.
# 1번으로 돌아간다.

# 0: 청소되지 않은 빈칸, 1: 벽
n, m = map(int, input().split())
r, c, d = map(int, input().split())

# 북0, 동1, 남2, 서3 - 상우하좌
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

# 방의 가장 북쪽, 가장 남쪽, 가장 서쪽, 가장 동쪽 줄 중 하나 이상에 위치한 모든 칸에는 벽이 있다
arr = [list(map(int, input().split())) for _ in range(n)]

def solve(cy, cx, dr):
    cnt = 0

    while True:     # 더 이상 움직이지 못할 때 종료
        arr[cy][cx] = 2     # 현재 위치 청소
        cnt += 1

        flag = True
        while flag:
            # 반시계 4방향으로 돌며 탐색
            for i in range(4):
                nd = (dr + 3 - i) % 4
                ny, nx = cy + dy[nd], cx + dx[nd]
                if arr[ny][nx] == 0:    # 청소가 안된 영역 => 이동
                    cy, cx, dr = ny, nx, nd
                    flag = False
                    break
            else:   # 네 방향 모두 미청소 영역 없음 -> 후진
                ty, tx = cy - dy[dr], cx - dx[dr]
                if arr[ty][tx] == 1:    # 벽이면 종료
                    return cnt
                else:
                    cy, cx = ty, tx

answer = solve(r, c, d)
print(answer)

