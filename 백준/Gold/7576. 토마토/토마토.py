# https://www.acmicpc.net/problem/7576
# 토마토 백준 7576

# 하루가 지나면, 익은 토마토들의 인접한 곳에 있는 익지 않은 토마토들은 익은 토마토의 영향을 받아 익게 된다.
# 며칠이 지나면 토마토들이 모두 익는지, 최소 일수 출력 -> bfs
import sys
from collections import deque
input = sys.stdin.readline

# 0: 익지 않은 토마토, 1: 익은 토마토, -1: 토마토가 들어있지 않은 칸
m, n = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

# 상하좌우
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

# 초기 토마토들을 q에 먼저 삽입
q = deque()
visited = [[0] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            q.append((i, j))
            visited[i][j] = 1

def bfs():
    while q:
        cy, cx = q.popleft()
        for dr in range(4): # 4방향
            ny, nx = cy + dy[dr], cx + dx[dr]
            # 범위 내, 미방문, 토마토가 익지 않았다면
            if 0 <= ny < n and 0 <= nx < m and visited[ny][nx] == 0 and arr[ny][nx] == 0:
                q.append((ny, nx))
                # 방문 배열에 날짜 저장
                visited[ny][nx] = visited[cy][cx] + 1
                arr[ny][nx] = 1

bfs()
# 처음부터 1부터 시작했으므로 마지막 출력할 때 -1
answer = max(map(max, visited)) - 1

# 토마토가 익지 않은 것이 있는지 확인 후 있으면 -1 출력
for i in range(n):
    for j in range(m):
        if arr[i][j] == 0:
            answer = -1
            break

print(answer)