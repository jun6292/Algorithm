# https://www.acmicpc.net/problem/11404
# 플로이드 백준 11404

import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
INF = int(1e9)
arr = [[INF] * (n + 1) for _ in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    # 같은 경로에 대해서 여러대의 버스가 있을 수 있다
    arr[a][b] = min(arr[a][b], c)

# 자기 자신으로 갈 수 없으므로 0
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == j:
            arr[i][j] = 0

# 플로이드 워셜 알고리즘
for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            arr[i][j] = min(arr[i][j], arr[i][k] + arr[k][j])

# i에서 j로 갈 수 없는 경우 -> INF: 0을 출력
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if arr[i][j] == INF:
            arr[i][j] = 0

for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(arr[i][j], end=" ")
    print()