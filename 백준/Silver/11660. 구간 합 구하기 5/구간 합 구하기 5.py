# 백준 11660 구간합구하기 5
import sys 
input = sys.stdin.readline

# N x N 배열, M: 합을 구하는 횟수
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
# DP 메모이제이션
memoi = [[0 for _ in range(N + 1)] for _ in range(N + 1)]

# 누적합 구하고 메모이제이션 적용
for i in range(1, N + 1):
    for j in range(1, N + 1):
        memoi[i][j] = memoi[i][j - 1] + memoi[i - 1][j] - memoi[i - 1][j - 1] + arr[i - 1][j - 1]

# 전부 더하고 부분 빼고 부분 빼고 두 번 뺀 부분 더하기
for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    sum = memoi[x2][y2] - memoi[x2][y1 - 1] - memoi[x1 - 1][y2] + memoi[x1 -1][y1 - 1]
    print(sum)