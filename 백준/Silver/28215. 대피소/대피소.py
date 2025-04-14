# https://www.acmicpc.net/problem/28215
# 대피소 백준 28215

# 맨해튼 거리, 가장 긴 거리가 최소가 되도록 대피소를 설치
# 그 때 대피소와 가장 멀리 떨어진 집과의 거리를 구하기
# 결국에 대피소까지 가장 먼 거리가 최소가 되도록 한다.
# 입력 값의 크기가 크지 않아서 브루트 포스로 진행

from itertools import combinations

# n개의 집, k개의 대피소
n, k = map(int, input().split())

# 집의 좌표 저장 [0]: 열, [1]: 행
arr = [list(map(int, input().split())) for _ in range(n)]

answer = INF = 300000
for comb in combinations(arr, k):
    distance = []
    for a in arr:
        min_dist = INF
        for c in comb:
            dist = abs(a[0] - c[0]) + abs(a[1] - c[1])
            min_dist = min(min_dist, dist)
        distance.append(min_dist)
    distance.sort()
    answer = min(answer, distance[-1])

print(answer)