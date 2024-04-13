N = int(input())
K = int(input())
board = [[0] * (N + 1) for _ in range(N + 1)]
direction_info = []

for _ in range(K):
    a, b = map(int, input().split())
    board[a][b] = 1

L = int(input())

for _ in range(L):
    x, c = input().split()
    direction_info.append((int(x), c))

# 동, 남, 서, 북
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def turn(direction, c):
    if c == 'L':
        direction = (direction - 1) % 4
    else:
        direction = (direction + 1) % 4
    return direction

def simulate():
    x, y = 1, 1 # 뱀의 머리 위치
    board[x][y] = 2 # 뱀의 존재 위치
    direction = 0  # 동쪽 방향
    time = 0    # 게임 시작 후 시간
    index = 0   # 다음에 회전할 정보
    q = [(x, y)]
    while True:
        # 이동 후
        nx = x + dx[direction]
        ny = y + dy[direction]
        # 맵 범위 안에 있고, 뱀의 몸통이 없는 위치
        if nx >= 1 and nx <= N and ny >= 1 and ny <= N and board[nx][ny] != 2:
            if board[nx][ny] == 0:  # 사과가 없다면 이동 후 꼬리 제거
                board[nx][ny] = 2
                q.append((nx, ny))
                px, py = q.pop(0)
                board[px][py] = 0
            if board[nx][ny] == 1: # 사과가 있다면 이동 후 꼬리 그대로 두기
                board[nx][ny] = 2
                q.append((nx, ny))
        # 벽이나 뱀의 몸통과 부딪힘
        else:
            time += 1
            break
        x, y = nx, ny
        time += 1
        if index < L and time == direction_info[index][0]:  # 회전할 시간인 경우 회전
            direction = turn(direction, direction_info[index][1])
            index += 1
    return time

print(simulate())
