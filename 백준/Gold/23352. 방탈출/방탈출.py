# https://www.acmicpc.net/problem/23352
# 방탈출 백준 23352

# 칸에는 0 ~ 9, 0이 적힌 방은 들어갈 수 없다
# 1) 임의의 방에서 다른 방으로 이동할 때 항상 최단 경로로 이동
# 2) 1을 만족하는 경로 중 가장 긴 경로의 시작 방과 끝 방에 적힌 숫자의 합
# 경로가 여러개면, 숫자의 합이 가장 큰 값이 비밀번호
from collections import deque

n, m = map(int, input().split())    # n x m
arr = [list(map(int, input().split())) for _ in range(n)]   # 방의 정보

answer = 0  # 비밀번호

# 상하좌우
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def bfs(y, x):
    visited = [[0] * m for _ in range(n)]
    q = deque()

    q.append((y, x))
    visited[y][x] = 1

    while q:
        cy, cx = q.popleft()
        flag = False

        for dr in range(4):
            ny, nx = cy + dy[dr], cx + dx[dr]
            # 범위 내, 미방문, 방의 번호가 0이 아니면
            if 0 <= ny < n and 0 <= nx < m and visited[ny][nx] == 0 and arr[ny][nx] > 0:
                q.append((ny, nx))
                visited[ny][nx] = visited[cy][cx] + 1
                flag = True

        if not flag:
            # [0]: 방의 시작 + 끝 합, [1]: 방의 시작부터 끝까지 거리
            sum_list.append((arr[cy][cx] + arr[y][x], visited[cy][cx]))

sum_list = []

for i in range(n):
    for j in range(m):
        if arr[i][j] > 0:
            bfs(i, j)

# 거리가 가장 멀고, 방의 합이 가장 큰 순으로 정렬
sum_list.sort(key=lambda x: (-x[1], -x[0]))
print(sum_list[0][0])