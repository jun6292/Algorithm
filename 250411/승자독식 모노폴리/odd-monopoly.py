# https://www.acmicpc.net/problem/19237
# 백준 19273 어른상어

# 상어 번호 1 이상 M 이하, 모든 번호는 고유
# 모든 상어는 자신의 위치에서 냄새를 뿌리고 1초마다 모든 상어가 이동한다. 그리고 다시 냄새 뿌린다
# 냄새는 상어가 k번 이동하면 사라진다
# 각 상어는 상하좌우로 이동하는데, 인접한 칸 중 아무 냄새가 없는 칸의 방향으로 이동한다.
# 그런 칸이 없으면 자신의 냄새가 있는 칸으로 이동한다. 이 때 가능한 칸이 여러 개라면, 우선순위를 따른다
# 우선순위는 상어마다 다르다. 같은 상어라도 상어가 보고 있는 방향에 따라 다르다.
# 상어가 맨 처음에 보고 있는 방향은 입력으로 주어지고, 그 후에는 방금 이동한 방향이 보고 있는 방향
# 모든 상어가 이동한 후 한 칸에 여러 마리의 상어가 남아있으면, 가장 작은 번호를 제외하고 모두 쫓겨난다

# 1번 상어만 격자에 남게 되기까지 몇 초가 걸리는지
answer = 0

# 1, 2, 3, 4
# 0, 위, 아래, 왼쪽, 오른쪽
dy = [0, -1, 1, 0, 0]
dx = [0, 0, 0, -1, 1]

n, m, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

shark = [[0] * 4 for _ in range(m)] # 상어 정보 저장 - 번호(sn), 위치(sy, sx), 방향(sd)
visited = [[[-1] * 2 for _ in range(n)] for _ in range(n)] # 상어 번호와 냄새 남은 시간을 추적

for i in range(n):
    for j in range(n):
        if arr[i][j] > 0:
            sn = arr[i][j] - 1
            shark[sn] = [sn, i, j, 0]
            visited[i][j][0], visited[i][j][1] = sn, k

first_dir = list(map(int, input().split()))
for i in range(m):
    shark[i][3] = first_dir[i]  # 상어 초기 방향 저장

# 상어 방향에 따른 우선순위 룩업 테이블
dir_table = [[[0] * 4 for _ in range(5)] for _ in range(m)]
for i in range(m):
    for j in range(1, 5):
        dir_table[i][j] = list(map(int, input().split()))

for answer in range(1, 1001):   # 1초 ~ 1001초
    # 각 상어 이동: 현재 방향 기준 빈칸 찾고, 빈칸이 없으면 자기냄새
    for i in range(len(shark)):
        sn, sy, sx, sd = shark[i]
        for dr in dir_table[sn][sd]:
            ny, nx = sy + dy[dr], sx + dx[dr]
            # 범위 내 냄새가 없는 경우: 빈칸 == -1
            if 0 <= ny < n and 0 <= nx < n and visited[ny][nx][0] == -1:
                shark[i] = [sn, ny, nx, dr]
                break
        else:   # 빈칸이 없는 경우: 냄새를 찾는다
            for dr in dir_table[sn][sd]:
                ny, nx = sy + dy[dr], sx + dx[dr]
                if 0 <= ny < n and 0 <= nx < n and visited[ny][nx][0] == sn:
                    shark[i] = [sn, ny, nx, dr]
                    break
    # 각 칸 냄새 -1
    for i in range(n):
        for j in range(n):
            if visited[i][j][0] != -1:  # 빈칸이 아닌 경우, 냄새가 있는 경우
                visited[i][j][1] -= 1
                if visited[i][j][1] == 0:  # 0되면 빈칸으로 처리
                    visited[i][j][0] = -1

    # 낮은 번호 상어부터 냄새 남긴다. 냄새가 있고, 내 냄새가 아니면 나는 삭제
    # 삭제는 for문으로 돌면 안된다.
    i = 0
    while i < len(shark):
        sn, sy, sx, sd = shark[i]
        # 냄새가 있고(빈칸이 아니면), 내 냄새 아니면(sn !=) 삭제
        if visited[sy][sx][0] != -1 and visited[sy][sx][0] != sn:
            shark.pop(i)
        else:   # 빈칸에 내가 처음 도달 => 새 냄새 남김
            visited[sy][sx] = [sn, k]
            i += 1

    if len(shark) <= 1: # 1마리 이하면 종료
        break

else:
    answer = -1

print(answer)