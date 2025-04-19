# https://www.acmicpc.net/problem/2667
# 단지번호붙이기 백준 2667

from collections import deque

# 총 단지 수, 단지내 집의 수를 오름차순 정렬하여 한 줄에 하나씩 출력
# 1: 집, 0: 집이 없는 곳
n = int(input())
arr = [list(map(int, input())) for _ in range(n)]

# 상하좌우
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def bfs(y, x):
    q = deque()
    house_cnt = 0

    q.append((y, x))
    visited[y][x] = 1
    house_cnt += 1

    while q:
        cy, cx = q.popleft()
        for dr in range(4):
            ny, nx = cy + dy[dr], cx + dx[dr]
            # 4방향, 범위 내, 미방문, 집이라면
            if 0 <= ny < n and 0 <= nx < n and visited[ny][nx] == 0 and arr[ny][nx] == 1:
                q.append((ny, nx))
                visited[ny][nx] = 1
                house_cnt += 1

    return house_cnt

visited = [[0] * n for _ in range(n)]
house = []
for i in range(n):
    for j in range(n):
        # 집이고 미방문이면 bfs
        if arr[i][j] == 1 and visited[i][j] == 0:
            cnt = bfs(i, j)
            house.append(cnt)

house.sort()
print(len(house))
for h in house:
    print(h)