# 지형은 각 변이 x축, y축과 평행한 직사각형이 겹쳐진 형태로 표현
# 캐릭터는 이 다각형의 둘레(굵은 선)를 따라서 이동
# 직사각형이 담긴 2차원 배열 rectangle, 초기 캐릭터의 위치 characterX, characterY, 아이템의 위치 itemX, itemY
# 캐릭터가 아이템을 줍기 위해 이동해야 하는 가장 짧은 거리를 return

# rectangle의 원소는 각 직사각형의 [좌측 하단 x, 좌측 하단 y, 우측 상단 x, 우측 상단 y]
from collections import deque

# 상하좌우
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

# 모든 직사각형의 좌표를 2배 해주는 것
# 왜냐하면, ㄷ 자 모양의 경우, 테두리를 따라 그리면 ㅁ 처럼 인식되어 착오가 있을 수 있기 때문에
def solution(rectangle, characterX, characterY, itemX, itemY):
    n = 102
    arr = [[-1] * n for _ in range(n)]
    visited = [[0] * n for _ in range(n)]
    
    for lx, ly, rx, ry in rectangle:
        lx, ly, rx, ry = lx * 2, ly * 2, rx * 2, ry * 2
        
        for i in range(ly, ry + 1):
            for j in range(lx, rx + 1):
                if ly < i < ry and lx < j < rx: # 사각형 내부
                    arr[i][j] = 0
                elif arr[i][j] != 0:    # 테두리인데 다른 사각형의 내부가 아닐 때
                    arr[i][j] = 1   # 진짜 테두리
    
    def bfs(y, x):
        q = deque()
        
        q.append((y, x))
        visited[y][x] = 1
        
        while q:
            cy, cx = q.popleft()
    
            for dr in range(4):
                ny, nx = cy + dy[dr], cx + dx[dr]
                if visited[ny][nx] == 0 and arr[ny][nx] == 1:
                    q.append((ny, nx))
                    visited[ny][nx] = visited[cy][cx] + 1
                    
        return visited[itemY * 2][itemX * 2] // 2
    
    return bfs(characterY * 2, characterX * 2)