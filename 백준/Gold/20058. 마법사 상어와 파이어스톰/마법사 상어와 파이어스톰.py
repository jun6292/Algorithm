# https://www.acmicpc.net/problem/20058
# 백준 20058 마법사 상어와 파이어스톰

# 상하좌우
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

# n: 격자 2^n, q: 파이어스톰 시전 횟수
n, q = map(int, input().split())
n = 2 ** n

# arr[r][c]는 얼음의 양, 0이면 얼음 없는 것
# 2차원 리스트를 0으로 감싼다 -> 행/열 + 2
arr = [[0] * (n + 2)] + [[0] + list(map(int, input().split())) + [0] for _ in range(n)] + [[0] * (n + 2)]

# 파이어스톰 시전 단계, 순서대로 q번
step = list(map(int, input().split()))

for L in step:
    L = 2 ** L
    # 2차원 리스트를 0으로 감싼다 -> 행/열 + 2
    tmp = [[0] * (n + 2) for _ in range(n + 2)]

    # 모든 부분 격자를 시계 방향으로 90도 회전
    for si in range(1, n + 1, L):
        for sj in range(1, n + 1, L):   # 가능한 모든 기준 위치
            for i in range(L):
                for j in range(L):
                    tmp[si + i][sj + j] = arr[si + L - 1 - j][sj + i]
    arr = tmp
    tmp = [x[:] for x in arr]   # 2차원 arr을 deepcopy, 라이브러리보다 빠름
    # 얼음이 있는 칸 3개 또는 그 이상과 인접해있지 않은 칸은 얼음의 양이 1 줄어든다.
    # => 인접해 있는 얼음이 2개 이하면(0이 2개 이상) 그 칸의 얼음의 양은 1 줄어든다.
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if arr[i][j] == 0:  # 얼음 아니면 넘어가고
                continue
            cnt = 0
            # 네 방향(범위 체크 필요 없다 -> 0으로 뚤러쌈) / 0이면 cnt += 1 / cnt >=2: 얼음 -= 1
            for dr in range(4):
                if arr[i + dy[dr]][j + dx[dr]] == 0:    # 얼음이 아니면
                    cnt += 1
                    if cnt >= 2:
                        tmp[i][j] -= 1  # 얼음 1 녹임
                        break
    arr = tmp

from collections import deque

def bfs(sy, sx):
    q = deque()

    q.append((sy, sx))
    visited[sy][sx] = 1
    cnt = 1

    while q:
        cy, cx = q.popleft()
        # 4방향, 미방문, 얼음이면 (>0)
        for dr in range(4):
            ny, nx = cy + dy[dr], cx + dx[dr]
            if visited[ny][nx] == 0 and arr[ny][nx] > 0:
                q.append((ny, nx))
                visited[ny][nx] = 1
                cnt += 1

    return cnt

# 얼음이 있는 칸이 얼음이 있는 칸과 인접해 있으면, 두 칸을 연결되어 있다고 한다.
visited = [[0] * (n + 2) for _ in range(n + 2)]
# 덩어리가 없으면 0 출력
answer = 0
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if visited[i][j] == 0 and arr[i][j] > 0:    # 미방문, 얼음일 경우
            answer = max(answer, bfs(i, j))

# 첫째 줄에 남아있는 얼음 arr[r][c]의 합을 출력
# 2차원 arr의 총합: sum(map(sum, arr))
print(sum(map(sum, arr)))
# 둘째 줄에 가장 큰 덩어리가 차지하는 칸의 개수를 출력
print(answer)

