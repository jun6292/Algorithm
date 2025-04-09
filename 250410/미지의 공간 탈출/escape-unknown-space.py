# https://www.codetree.ai/ko/frequent-problems/problems/escape-unknown-space/description
# 코드트리 미지의 공간 탈출

# 빈 공간 0, 장애물 1 - 타임머신은 빈 공간만 이동 가능
# 타임머신은 시간의 벽의 윗면 어딘가에 위치
# 시간의 벽과 맞닿은 미지의 공간의 바닥은 장애물들로 둘러 쌓여 있으나, 단 한 칸만 빈 공간
# 미지의 공간 바닥에는 F개의 시간 이상 현상 존재(v의 배수 턴마다 확산) - 빈 공간으로만 확산되며 확산 안되면 멈춘다
# 동서남북(0123)
# 타임머신은 매 턴마다 상하좌우로 한 칸씩 이동할 수 있으며, 장애물과 시간 이상 현상을 피해 탈출
# 타임머신이 시작부터 탈출구까지 이동하는 데 필요한 최소 턴 수를 출력, 탈출 불가능할 경우 -1 출력
# 시간 이상 현상이 확산된 직후 타임머신이 이동

# 미지의 공간 한변의 길이 n, 시간의 벽 한 변의 길이 m, 시간 이상 현상 개수 f
n, m, f = map(int, input().split())
unknown_2d = [list(map(int, input().split())) for _ in range(n)]

# 시간의 벽 동-서-남-북-윗면의 단면도
time_wall_3d = [[list(map(int, input().split())) for _ in range(m)] for _ in range(5)]

# 초기 위치 r, c / 확산방향 d / 확산상수 v -> [r, c, d, v]
time_outlier = [list(map(int, input().split())) for _ in range(f)]

def find_3d_start():
    for i in range(m):
        for j in range(m):
            if time_wall_3d[4][i][j] == 2:
                return 4, i, j

def find_2d_end():
    for i in range(n):
        for j in range(n):
            if unknown_2d[i][j] == 4:
                unknown_2d[i][j] = 0
                return i, j

def find_3d_base():
    for i in range(n):
        for j in range(n):
            if unknown_2d[i][j] == 3:
                return i, j

def find_3d_end_2d_start():
    # 3차원 시작 좌표(base) 찾기
    bi, bj = find_3d_base()

    # 3차원 좌표에서 2차원 연결 좌표 찾기 - 1차 목적지
    for i in range(bi, bi + m):
        for j in range(bj, bj + m):
            if unknown_2d[i][j] != 3:   # 3차원 시간의 벽이 아님
                continue
            # 우측에 2차원 시작점 존재 (동 0)
            if unknown_2d[i][j + 1] == 0:
                return 0, m - 1, (m - 1) - (i - bi), i, j + 1
            # 좌측에 2차원 시작점 존재 (서 1)
            elif unknown_2d[i][j - 1] == 0:
                return 1, m - 1, i - bi, i, j - 1
            # 하측 2차원 시작점 존재 (남 2)
            elif unknown_2d[i + 1][j] == 0:
                return 2, m - 1, j - bj, i + 1, j
            # 상측에 2차원 시작점 존재 (북 3)
            elif unknown_2d[i - 1][j] == 0:
                return 3, m - 1, (m - 1) - (j - bj), i - 1, j

from collections import deque

# 상하좌우
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def bfs_3d(sk, si, sj, ek, ei, ej):
    q = deque()
    v = [[[0] * m for _ in range(m)] for _ in range(5)]

    q.append((sk, si, sj))
    v[sk][si][sj] = 1

    while q:
        ck, ci, cj = q.popleft()

        if (ck, ci, cj) == (ek, ei, ej):
            return v[ck][ci][cj]

        # 4방향, 범위내/범위밖 => 다른 평면 이동처리, 미방문
        for dr in range(4):
            ni, nj = ci + dy[dr], cj + dx[dr]
            # 범위 밖
            if ni < 0:  # 위쪽 범위 이탈
                if ck == 0:
                    nk, ni, nj = 4, (m - 1) - cj, m - 1
                elif ck == 1:
                    nk, ni, nj = 4, cj, 0
                elif ck == 2:
                    nk, ni, nj = 4, m - 1, cj
                elif ck == 3:
                    nk, ni, nj = 4, 0, (m - 1) - cj
                elif ck == 4:
                    nk, ni, nj = 3, 0, (m - 1) - cj
            elif ni >= m:   # 아래쪽 범위 이탈
                if ck == 4:
                    nk, ni, nj = 2, 0, cj
                else:
                    continue
            elif nj < 0:    # 왼쪽 범위 이탈
                if ck == 4:
                    nk, ni, nj = 1, 0, ci
                elif ck == 0:
                    nk, ni, nj = 2, ci, m - 1
                elif ck == 1:
                    nk, ni, nj = 3, ci, m - 1
                elif ck == 2:
                    nk, ni, nj = 1, ci, m - 1
                elif ck == 3:
                    nk, ni, nj = 0, ci, m - 1
            elif nj >= m:   # 오른쪽 범위 이탈
                if ck == 4:
                    nk, ni, nj = 0, 0, (m - 1) - ci
                elif ck == 0:
                    nk, ni, nj = 3, ci, 0
                elif ck == 1:
                    nk, ni, nj = 2, ci, 0
                elif ck == 2:
                    nk, ni, nj = 0, ci, 0
                elif ck == 3:
                    nk, ni, nj = 1, ci, 0
            else:   # 범위 내, 같은 평면
                nk = ck

            # 미방문, 조건 맞으면
            if v[nk][ni][nj] == 0 and time_wall_3d[nk][ni][nj] == 0:
                q.append((nk, ni, nj))
                v[nk][ni][nj] = v[ck][ci][cj] + 1

def bfs_2d(v, dist, si, sj, ei, ej):
    q = deque()

    q.append((si, sj))
    v[si][sj] = dist

    while q:
        ci, cj = q.popleft()

        if (ci, cj) == (ei, ej):
            return v[ci][cj]

        # 4방향, 범위내, 미방문, 조건(v[ci][cj] < v[ni][nj])
        for dr in range(4):
            ni, nj = ci + dy[dr], cj + dx[dr]
            if 0 <= ni < n and 0 <= nj < n and unknown_2d[ni][nj] == 0 and v[ci][cj] + 1 < v[ni][nj]:
                q.append((ni, nj))
                v[ni][nj] = v[ci][cj] + 1

    # 목적지를 찾을 수 없는 경우
    return -1

# 1) 좌표찾기
# 3차원 시작/끝, 2차원 시작/끝 좌표 탐색

# 3차원 시작 좌표 탐색
sk_3d, si_3d, sj_3d = find_3d_start()

# 2차원 끝 좌표 탐색
ei, ej = find_2d_end()

# 3차원 끝, 2차원 시작 좌표 탐색
# 평면 / 3차원 종료 좌표 i, j / 2차원 시작 좌표 i, j
ek_3d, ei_3d, ej_3d, si, sj = find_3d_end_2d_start()

# 2) 3차원 공간 탐색: 시작위치 -> 탈출위치 탐색(BFS 최단거리)
dist = bfs_3d(sk_3d, si_3d, sj_3d, ek_3d, ei_3d, ej_3d)
# print(dist)
# 3) 2차원 탐색 준비: 시간이상 현상 처리해서 visited에 시간 표시
# 동 서 남 북
di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]
v = [[401] * n for _ in range(n)]
for wi, wj, wd, wv in time_outlier: # 시간 단위로 wd 방향으로 확산표시(출구가 아닌 경우만 확산)
    v[wi][wj] = 1
    for mul in range(1, n + 1):
        wi, wj = wi + di[wd], wj + dj[wd]
        if 0 <= wi < n and 0 <= wj < n and unknown_2d[wi][wj] == 0 and (wi, wj) != (ei, ej):
            if v[wi][wj] > wv * mul:    # 겹칠 수 있으니 더 큰 값 일때만 갱신
                v[wi][wj] = wv * mul
        else:
            break

# 4) 2차원 시작 위치에서 BFS로 탈출구 탐색(visited에 적혀 있는 값보다 작아야)
dist = bfs_2d(v, dist, si, sj, ei, ej)

print(dist)