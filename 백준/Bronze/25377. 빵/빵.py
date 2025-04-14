# https://www.acmicpc.net/problem/25377
# 빵 백준 25377

# 빵이 가게에 도착하는 순간이나 도착하기 전에 가게에 갈 수 있으면 KOI 빵을 살 수 있고,
# 빵이 도착한 이후에 가게에 가면 이미 늦어서 빵이 없다.

# 가게의 수
n = int(input())
answer = 1001

# a: 가게까지 가는 데 걸리는 시간, b: 빵이 들어올 때까지 시간
for _ in range(n):
    a, b = map(int, input().split())
    if a <= b:
        answer = min(answer, b)

# KOI 빵을 살 수 없다면, -1을 출력, 살 수 있다면, 현재 시점에서 빵을 구하는 데 걸리는 최소 시간을 출력
if answer == 1001:
    answer = -1

print(answer)

