# https://www.acmicpc.net/problem/19236
# https://www.codetree.ai/ko/frequent-problems/problems/odd-chess2/description
# 백준 19236 청소년 상어
# 코드트리 술래잡기 체스

# 4x4, 칸 마다 물고기 1마리, 물고기마다 고유의 번호 1 ~ 16, 8방향 - 상하좌우, 대각선
# 청소년 상어 (0, 0) 시작, 물고기를 먹고 해당 방향 가짐, 이후 물고기 이동
# 번호가 작은 물고기부터 순서대로 이동, 물고기는 한 칸 이동 - 빈 칸 or 다른 물고기가 있는 칸
# 상어가 있거나 공간의 경계를 넘는 칸으로 이동 불가능
# 이동 불가능한 경우 45도 반시계 방향으로 틈, 이동할 수 있는 칸이 없으면 이동하지 않는다
# 다른 물고기가 있는 칸으로 이동할 때는 서로의 위치를 바꾼다
# 물고기 이동이 끝나면 상어가 이동한다.
# 상어는 방향에 있는 칸으로 이동, 한 번에 여러 개의 칸을 이동할 수 있다.
# 물고기 있는 칸으로 이동했으면, 물고기를 먹고, 그 물고기의 방향을 갖는다.
# 이동 중에 지나가는 칸에 있는 물고기는 먹지 않으며, 물고기가 없는 칸으로 이동할 수 없다.
# 상어가 이동할 수 있는 칸이 없으면 집으로 가며, 상어 이동 후에는 다시 물고기가 이동한다.

import copy

# 상어가 먹을 수 있는 물고기 번호의 합의 최댓값
answer = 0

# 방향은 1 ~ 8, 상부터 반시계 방향으로 45도 꺾여감
# 상 좌상 좌 좌하 하 우하 우 우상
dy = [-1, -1, 0, 1, 1, 1, 0, -1]
dx = [0, -1, -1, -1, 0, 1, 1, 1]

def find_fish(idx, t_arr):
    for i_ in range(4):
        for j_ in range(4):
            if idx == t_arr[i_][j_][0]:
                return i_, j_, t_arr[i_][j_][1]

def dfs(sy, sx, sd, sm, p_arr):
    # 매번 정답 갱신
    global answer
    answer = max(answer, sm)

    # 물고기 이동 (1 ~ 16): 기준은 arr이므로 먼저
    for num in range(1, 17):
        cy, cx, cd = find_fish(num, p_arr)
        if cd == -1:    # 물고기가 없는 경우
            continue
        for dr in range(8):  # 현재 방향부터 8방향 체크
            tmp_d = (cd + dr) % 8
            ny, nx = cy + dy[tmp_d], cx + dx[tmp_d]
            # 범위 내 & 상어가 아니면(빈칸 or 물고기)
            if 0 <= ny < 4 and 0 <= nx < 4 and (ny, nx) != (sy, sx):
                p_arr[cy][cx][1] = tmp_d
                p_arr[cy][cx], p_arr[ny][nx] = p_arr[ny][nx], p_arr[cy][cx]
                break

    # 상어 이동 (1 ~ 3칸)
    for s in range(1, 4):
        nsy, nsx = sy + dy[sd] * s, sx + dx[sd] * s
        # 범위 내, 물고기라면
        if 0 <= nsy < 4 and 0 <= nsx < 4 and p_arr[nsy][nsx][1] != -1:
            fn, fd = p_arr[nsy][nsx]
            p_arr[nsy][nsx][1] = -1     # 물고기를 먹는다

            # 물고기 이동 원상복구 복잡하므로 차라리 복사해서 넘김
            dfs(nsy, nsx, fd, sm + fn, copy.deepcopy(p_arr))

            p_arr[nsy][nsx][1] = fd    # 원상복구

arr = [[[0] * 2 for _ in range(4)] for _ in range(4)]
for i in range(4):
    fish_list = list(map(int, input().split()))
    for j in range(4):
        arr[i][j] = [fish_list[j*2], fish_list[j*2+1] - 1]  # 번호[0], 방향[1]

# 상어 초기 위치 물고기 먹음
fish_num, fish_dir = arr[0][0]
arr[0][0][1] = -1   # (0, 0) 위치 물고기 먹음 처리

dfs(0, 0, fish_dir, fish_num, arr)  # 상어 위치, 방향, 초기 점수, arr 전달
print(answer)