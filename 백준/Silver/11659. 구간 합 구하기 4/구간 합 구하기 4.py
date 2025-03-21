# https://www.acmicpc.net/problem/11659
# 백준 11659 구간합 구하기 4

import sys
input = sys.stdin.readline

n, m = map(int, input().split())

arr_sum = list(map(int, input().split()))

for i in range(1, len(arr_sum)):
    arr_sum[i] = arr_sum[i - 1] + arr_sum[i]

for _ in range(m):
    start, end = map(int, input().split())
    if start == 1:
        answer = arr_sum[end - 1]
    else:
        answer = arr_sum[end - 1] - arr_sum[start - 2]
    print(answer)

