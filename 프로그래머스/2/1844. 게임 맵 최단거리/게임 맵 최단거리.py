from collections import deque

# 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y, maps):
    N = len(maps)
    M = len(maps[0])
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= N or ny >= M: continue
            if maps[nx][ny] == 0: continue
            if maps[nx][ny] == 1:
                maps[nx][ny] = maps[x][y] + 1
                queue.append((nx, ny))  
    return maps[N - 1][M - 1] 
    
def solution(maps):
    answer = bfs(0, 0, maps)
    return -1 if answer == 1 else answer