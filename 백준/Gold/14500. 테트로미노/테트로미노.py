# https://www.acmicpc.net/problem/14500
# 테트로미노 백준 14500

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

# 가능한 모든 패턴의 회전/대칭 좌표(3개)를 저장
tet = [[(0, 1), (0, 2), (0, 3)],[(1, 0), (2, 0), (3, 0)], # ㅣ(회전)
	[(0, 1), (1, 0), (1, 1)],  # ㅁ
    [(1, 0), (2, 0), (2, 1)], [(0, 1), (0, 2), (1, 0)], [(0, 1), (1, 1), (2, 1)], [(0, 1), (0, 2),(-1, 2)], # ㄴ (회전)
    [(0, 1),(-1, 1),(-2, 1)], [(1, 0), (1, 1), (1, 2)], [(0, 1), (1, 0), (2, 0)], [(0, 1), (0, 2), (1, 2)], # ㄴ 대칭(회전)
    [(1, 0), (1, 1), (2, 1)], [(0, 1),(-1, 1),(-1, 2)],   # ㄹ(회전)
    [(1, 0), (0, 1),(-1, 1)], [(0, 1), (1, 1), (1, 2)],   # ㄹ 대칭(회전)
    [(0, 1), (0, 2), (1, 1)], [(-1, 1),(0, 1), (1, 1)], [(0, 1), (0, 2),(-1, 1)], [(1, 0), (2, 0), (1, 1)]] # ㅏ(회전)

def cal(y, x, loc):
    tmp = arr[y][x]
    for dy, dx in loc:
        ny, nx = y + dy, x + dx
        if 0 <= ny < n and 0 <= nx < m:
            tmp += arr[ny][nx]
        else:
            return 0
    return tmp

answer = 0
for i in range(n):
    for j in range(m):
        for pos in tet:
            sm = cal(i, j, pos)
            answer = max(answer, sm)

print(answer)