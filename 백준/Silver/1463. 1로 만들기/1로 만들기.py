# https://www.acmicpc.net/problem/1463
# 1로 만들기 백준 1463

# X가 3으로 나누어 떨어지면, 3으로 나눈다.
# X가 2로 나누어 떨어지면, 2로 나눈다.
# 1을 뺀다.
# 연산을 사용하는 횟수의 최솟값을 출력
import sys
input = sys.stdin.readline

n = int(input())

dp = [0] * (n + 1)
for i in range(2, n + 1):
    dp[i] = dp[i - 1] + 1
    if i % 2 == 0:  # 2의 배수인 경우
        dp[i] = min(dp[i], dp[i // 2] + 1)
    if i % 3 == 0:  # 3의 배수인 경우
        dp[i] = min(dp[i], dp[i // 3] + 1)

print(dp[n])