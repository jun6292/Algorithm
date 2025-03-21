# https://www.acmicpc.net/problem/21921
# 백분 21921 블로그

n, x = map(int, input().split())
visitors = list(map(int, input().split()))

sliding_window = sum(visitors[:x])
max_sum = sliding_window
max_cnt = 1

for start in range(x, n):
    sliding_window -= visitors[start - x]
    sliding_window += visitors[start]

    if max_sum < sliding_window:
        max_cnt = 1
        max_sum = sliding_window
    elif max_sum == sliding_window:
        max_cnt += 1

if max_sum == 0:
    print('SAD')
else:
    print(max_sum)
    print(max_cnt)