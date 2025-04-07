# https://www.acmicpc.net/problem/16236
# 백준 16236 아기 상어

# 한 칸에는 물고기가 최대 1마리 존재
# 아기 상어 크기: 2에서 시작, 1초에 상하좌우 인접한 한 칸 이동
# 아기 상어는 자기보다 큰 물고기가 있는 칸은 지나갈 수 없다. 크기가 작은 물고기만 섭취 가능
# 크기가 같은 물고기는 먹을 수 없고, 지나갈 수만 있다.

# 더 이상 먹을 수 있는 물고기가 공간에 없다면 아기 상어는 엄마 상어에게 도움 요청
# 먹을 수 있는 물고기가 1마리면, 먹으러 간다
# 먹을 수 있는 물고기가 1마리보다 많다면 가장 가까운 물고기를 먹으러 간다
# 물고기와의 거리는 지나야 하는 칸의 개수 최솟값
# 거리가 가까운 물고기가 많다면, 가장 위에 있는 물고기, 여러마리면 가장 왼쪽에 있는 물고기 섭취
# 이동은 1초 소요
# 자신의 크기와 같은 수의 물고기를 먹을 때마다 크기가 1증가

from collections import deque

n = int(input())
space = [list(map(int, input().split())) for _ in range(n)]

# 상하좌우
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

answer = 0  # 이동거리
baby_shark_size = 2 # 아기상어 크기
eat_cnt = 0 # 먹은 횟수

# 아기 상어의 초기 위치 찾기
cy, cx = 0, 0
for i in range(n):
    for j in range(n):
        if space[i][j] == 9:
            cy, cx = i, j
            space[i][j] = 0
            break

def bfs(sy, sx):
    # 1) 큐, v[], 필요 자료형 생성
    q = deque()
    v = [[0] * n for _ in range(n)]
    _eat_list = []

    # 2) 큐에 초기 데이터 삽입, v 표시
    q.append((sy, sx))
    v[sy][sx] = 1
    eat_distance = 0

    while q:
        ty, tx = q.popleft()    # 큐에서 데이터 하나 꺼냄

        # eat_distance에 적힌 거리는 모두 큐에 넣었다는 의미
        if eat_distance == v[ty][tx]:
            return _eat_list, eat_distance - 1

        # 4방향, 범위 내, 미방문, 조건(나보다 같거나 작은 물고기) => 이동할 수 있음
        for i in range(4):
            ny, nx = ty + dy[i], tx + dx[i]
            if 0 <= ny < n and 0 <= nx < n and v[ny][nx] == 0 and baby_shark_size >= space[ny][nx]:
                q.append((ny, nx))
                v[ny][nx] = v[ty][tx] + 1   # 이동거리 1 증가
                # 나보다 작은 물고기인 경우 eat_list에 추가
                if 0 < space[ny][nx] < baby_shark_size:
                    _eat_list.append((ny, nx))
                    eat_distance = v[ny][nx]

    # 방문을 모두 끝낸경우(먹을 물고기를 못찾은 경우)
    return _eat_list, eat_distance - 1

while True:
    eat_list, dist = bfs(cy, cx)
    if len(eat_list) == 0:  # 더 이상 먹을 물고기가 없을 때
        break

    eat_list.sort(key=lambda x: (x[0], x[1]))   # 가장 위쪽, 가장 아래쪽 물고기
    cy, cx = eat_list[0]
    space[cy][cx] = 0
    eat_cnt += 1        # 물고기 먹음
    answer += dist      # 이동거리 추가

    if eat_cnt == baby_shark_size:
        baby_shark_size += 1    # 상어크기만큼 물고기 먹었을 때 상어크기 증가
        eat_cnt = 0

print(answer)